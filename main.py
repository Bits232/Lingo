import flet as ft
from database import init_db, load_lang, insert, delete_lang
from home import HomePage
from subcategory_page import SubCategoryPage
from course_page import CoursePage

languages = ['english', 'yoruba', 'spanish','Hindi','Swahili','Tagalog']

def main(page: ft.Page):
    page.title = "Local Learning App"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll='adaptive'

    init_db()

    lang_dropdown = ft.Dropdown(
        label="Select Language",
        options=[ft.dropdown.Option(l) for l in languages],
        width=300
    )
    continue_button = ft.ElevatedButton("Continue")

    ui_texts = {
        "english": {
            "choose_language": "Choose your language",
            "select_language": "Select Language",
            "continue": "Continue",
            "please_select": "Please select a language"
        },
        "spanish": {
            "choose_language": "Elige tu idioma",
            "select_language": "Seleccionar idioma",
            "continue": "Continuar",
            "please_select": "Por favor seleccione un idioma"
        },
        "yoruba": {
            "choose_language": "Yan ede re",
            "select_language": "Yan Ede",
            "continue": "Tesiwaju",
            "please_select": "Jowo yan ede"
        }
    }

    def go_to_home():
        page.go('/home')

    def on_continue_click(e):
        lang = lang_dropdown.value
        if not lang:
            current_lang = load_lang() or 'english'
            page.snack_bar = ft.SnackBar(ft.Text(ui_texts[current_lang]["please_select"]))
            page.snack_bar.open = True
            page.update()
            return
        insert(lang)
        go_to_home()

    def on_route_change(e):
        page.clean()
        lang = load_lang()

        
        if not lang:
            selected_texts = ui_texts["english"] 
            lang_dropdown.label = selected_texts["select_language"]
            continue_button.text = selected_texts["continue"]
            continue_button.on_click = on_continue_click

            page.controls.append(
                ft.Column(
                    [
                        ft.Text(selected_texts["choose_language"], size=22, weight='bold'),
                        lang_dropdown,
                        continue_button
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        else:
            selected_texts = ui_texts.get(lang, ui_texts["english"])
            lang_dropdown.label = selected_texts["select_language"]
            continue_button.text = selected_texts["continue"]

            if page.route.startswith("/home"):
                page.controls.append(HomePage(page))
            elif page.route.startswith("/subcategory"):
                category_data = page.client_storage.get("category_data")
                page.controls.append(SubCategoryPage(category_data))
            elif page.route.startswith("/course"):
                subcategory_data = page.client_storage.get("subcategory_data")
                page.controls.append(CoursePage(subcategory_data))
            else:
                page.go("/home")  

        page.update()

    page.on_route_change = on_route_change
    page.go(page.route)

ft.app(target=main)
