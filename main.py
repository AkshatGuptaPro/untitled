def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_string("HELLO")
basic.show_string("LETS PLAY")