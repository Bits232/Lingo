import flet as ft

class CoursePage(ft.UserControl):
    def __init__(self, subcategory_data):
        super().__init__()
        self.subcategory = subcategory_data

    def build(self):
        lessons_widgets = []

        for lesson in self.subcategory["lessons"]:
            lessons_widgets.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(lesson["title"], weight="bold", size=18),
                        ft.Text(lesson["content"], size=14)
                    ], expand=True),
                    padding=15
                )
            )

        return ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=self.go_back),
                        ft.Text(f"Subcategory: {self.subcategory['subcategory']}", weight="bold", size=22)
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                ft.Column(lessons_widgets, scroll=ft.ScrollMode.AUTO)
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def go_back(self, e):
        self.page.go("/subcategory")
