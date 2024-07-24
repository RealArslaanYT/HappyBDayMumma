import flet as ft
import threading


def main(page: ft.Page) -> None:
    page.title = "Happy Birthday!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.title_bar_buttons_hidden = True
    page.window.title_bar_hidden = True

    def video_ended():
        page.clean()
        image = ft.Image(
            src="https://cdn-icons-png.flaticon.com/512/6003/6003502.png",
            width=page.width / 2,
            height=page.height / 2
        )
        text2 = ft.Text("Love you!\n- From Arslaan", size=45, text_align=ft.TextAlign.CENTER, width=page.width / 2)
        page.add(ft.Row(
                [
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    image
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    text2
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    def check_video_status():
        while True:
            if video.is_completed(10000):
                video_ended()
                break

    def play_video(e):
        page.clean()
        page.add(
            ft.Row(
                [video_container],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    def startVideoThread():
        threading.Thread(target=check_video_status, daemon=True).start()

    media = [
        ft.VideoMedia(
            "https://raw.githubusercontent.com/RealArslaanYT/VideoHost/main/HappyBDayMumma.mp4"
        )
    ]

    text = ft.Text("Happy Birthday,\nMumma!", size=45, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, width=page.width / 2)
    video = ft.Video(
            expand=True,
            playlist=media,
            playlist_mode=ft.PlaylistMode.NONE,
            fill_color=ft.colors.BLACK,
            volume=100,
            autoplay=True,
            aspect_ratio=9/16,
            height=page.height,
            show_controls=False,
            filter_quality=ft.FilterQuality.HIGH,
            muted=False,
            on_loaded=lambda e: startVideoThread()
    )
    video_container = ft.Container(
        content=video,
        expand=True,
        width=page.width,
        height=page.height
    )

    button = ft.ElevatedButton(text="Start!", width=page.width / 2, height=100, on_click=play_video)
    page.add(
        ft.Row(
            [
                ft.Column([
                        ft.Column(
                            [
                                text
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        button
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(name="", target=main, view=None, host="0.0.0.0", port=8080)
