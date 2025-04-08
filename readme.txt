Automatic shiny hunting program for static encounters - generations 2-4

INTRODUCTION
This tool is meant to automatically shiny-hunt static encounters in all Pokémon games that feature static sprites in battle. It's designed for streamers that want to shiny hunt in front of their audience without spending hours mashing buttons.
Currently tested on the static Lapras in Union Cave in Pokémon Crystal.

SETUP
There's quite some setup to be done as the program was originally designed for a specific hunt. It's nothing complicated, but it must be done in order to guarantee correct functionality.

On your device, create a folder in which to store all the files required for the program. Make sure all the libraries required are properly installed.


1) Setting up the image detection

The program has no idea of what a shiny Pokémon is, so we will have to do some introduction work first.

Open your game within the stream layout, and trigger a wild encounter with your desired target. When the appearance animation ends, take a screenshot of the ENTIRE screen by pressing Windows + Print, or by using Windows's snipping tool. Keep the game open in the background.

Open the screenshot you just took in MS Paint and select the area around the wild encounter. Write down the x/y coordinates of the top-left point, as well as the width and height of the selected area. You can now close MS Paint.

Open both "getimages.py" and "shiny.py" with your text editor of choice. Find the "screen_region" tuple declaration in both files and replace the values (which should default to 1, 2, 3, 4) in this order:

- x coordinate of the top-left corner
- y coordinate of the top-left corner
- width of the selected area
- height of the selected area.

Save both files, then close "shiny.py".

Start "getimages.py" and reopen your game, which should still be in the wild battle where you left it.
A rectangle should appear over the region you specified, and "getimages.py" will save a screenshot of that area named "debug_screenshot.jpg". If the area doesn't align, adjust the values in screen_region as needed.
If you're satisfied with the screenshot, move it to the folder where the program is stored (any folder works, but let's keep it simple) and rename it "normal.jpg".

Now the program knows what a regular encounter is.

Use a GameShark code or similar to force a shiny encounter, then run "getimages.py" again. Move the newly acquired debug screenshot in the same folder as the other one and rename it "shiny.jpg". While you may argue this defeats the purpose of the hunt, this ensures that the program will work on the correct source material, and you can remove the cheat right after.

We can now ditch "getimages.py".

Open "shiny.py" and replace the values for "normal_image_path" and "shiny_image_path" with the paths of the two images we just took.

2) Setting up the actual hunt

Now that the program knows what a shiny Pokémon is, let's tell them how to shiny hunt for you.

We will be modifying the elements of "sequence_1" and "sequence_reset" according to the game you're playing.

Every instruction in the sequences is a tuple (button, how long is it held down, how much time must pass until the next input).
We can ignore the second element as it isn't important.

In sequence_1, change the first element of the only instruction available to the key your A button is mapped to, and the third to a sufficient number of seconds for the wild encounter animation to fully end. This value scales if you plan on speeding up the game.

In sequence_reset, change the first instruction's first element to the keyboard shortcut for the reset button. For every time you need to press A in order to get through the intro cutscene and start another encounter, add another tuple starting with your A button and appropriate timing. 
Save and close "shiny.py" afterwards.

Once all of this is done, the program is ready to go!

3) Executing the program

Start the game and have your character stand directly in front of the encounter you're trying to hunt. Start "shiny.py" and return to the game.

The program will start the encounter, then wait for the animation to end according to the timing you gave them.

If the region you defined matches "normal.jpg" or anything else, the program will enter the sequence to reset the game, then retry.

If the region you defined matches "shiny.jpg", the program will terminate, allowing you to move on with the capture on your terms.