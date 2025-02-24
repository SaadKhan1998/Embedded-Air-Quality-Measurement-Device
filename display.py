# display.py - Handles visualization on LED Matrix and Seven-Segment Display

from Adafruit_LED_Backpack import SevenSegment
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas
import numpy as np

# Initialize Seven-Segment Display
svn_seg = SevenSegment.SevenSegment(address=0x70)
svn_seg.begin()

# Initialize LED Matrix Display
my_spi = spi(port=0, device=1, gpio=noop())
my_led = max7219(my_spi, cascaded=1, block_orientation=90, rotate=0)

def clearscreen():
    """Clear the Seven-Segment Display."""
    svn_seg.clear()
    svn_seg.write_display()

def svnseg_print(num):
    """Print number on Seven-Segment Display."""
    clearscreen()
    num = round(num, 2)
    svn_seg.print_number_str(str(num))
    svn_seg.write_display()

def draw_led_plot(draw_list, graph_position):
    """Draw AQI trend on LED matrix."""
    with canvas(my_led) as draw:
        draw.point((graph_position, 0), fill="white")
        for index, value in enumerate(draw_list):
            draw.point((index, 8 - value), fill="white")

def graph_counter(move, graph_position):
    """Navigate through different visualized parameters."""
    if move == "right":
        return (graph_position + 1) % 5
    elif move == "left":
        return (graph_position - 1) % 5
    return graph_position


