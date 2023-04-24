//  game starts here
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    //  function/subroutine called "on_button_pressed_a" (when button is pressed)
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.SmallHeart)
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.SmallHeart)
    if (Math.randomBoolean()) {
        //  if statement that generates a random True of False
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
    
})
