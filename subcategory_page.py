import flet as ft

class SubCategoryPage(ft.UserControl):
    def __init__(self, category_data):
        super().__init__()
        self.category_data = category_data

    def build(self):
        subcategory_widgets = []

        for subcategory in self.category_data["subcategories"]:
            subcategory_widgets.append(
                ft.Card(
                    content=ft.Container(
                        padding=10,
                        content=ft.Column([
                            ft.ListTile(title=ft.Text(subcategory["subcategory"])),
                            ft.TextButton('Take Course', on_click=lambda e, s=subcategory: self.open_course(s))
                        ])
                    )
                )
            )

        return ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.go_back),
                        ft.Text(f"Category: {self.category_data['category']}", weight="bold", size=22)
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                ft.Column(subcategory_widgets, scroll=ft.ScrollMode.AUTO)
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def open_course(self, subcategory_data):
        self.page.client_storage.set("subcategory_data", subcategory_data)
        self.page.go("/course")

    def go_back(self, e):
        self.page.go("/home")
