def on_button_pressed_a():

    # function/subroutine called "on_button_pressed_a" (when button is pressed)

    basic.show_icon(IconNames.HEART)

    basic.show_icon(IconNames.SMALL_HEART)

    basic.show_icon(IconNames.HEART)

    basic.show_icon(IconNames.SMALL_HEART)

    if Math.random_boolean():

        # if statement that generates a random True of False

        basic.show_icon(IconNames.HAPPY)

    else:

        basic.show_icon(IconNames.SAD)

 
 

# game starts here

input.on_button_pressed(Button.A, on_button_pressed_a)
