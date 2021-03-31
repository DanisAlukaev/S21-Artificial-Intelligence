import cairo
import numpy as np
from modules.art_evolution.models import Individual


def restore_image(individual: Individual):
    """
    Method restoring image according to passed chromosome.
    To draw the image was utilized cairo package that is more efficient compared to PIL.
    :param individual: member of the population.
    :return: RGBA numpy array.
    """
    # create RGBA image surface
    image_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, *individual.image_size)
    context = cairo.Context(image_surface)
    # use Arial font to draw characters
    context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

    # represent each gene in the chromosome
    for symbol in individual.chromosome:
        # set the font side on the image surface
        context.set_font_size(symbol['font_size'])
        # get the RGBA parameters for the symbol
        red, green, blue, alpha = symbol['color']
        # set the RGB parameter to draw the symbol
        context.set_source_rgb(red / 255, green / 255, blue / 255)
        # move cursor to position of symbol to be drawn
        context.move_to(*symbol['position'])
        # draw the symbol
        context.show_text(symbol['symbol'])

    # for image surface there was allocated space on the heap
    # use the pointer to access data stored in the memory area
    buffer = image_surface.get_data()
    image = np.ndarray(shape=(*individual.image_size, 4), dtype=np.uint8, buffer=buffer)
    return image
