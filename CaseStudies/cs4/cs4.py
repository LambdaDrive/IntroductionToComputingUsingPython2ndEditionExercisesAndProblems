##################################
# Solution to Practice Problem #
##################################


# Practice Problem CS.18
import PIL.Image, PIL.ImageFilter

def warhol(photo):
    '''returns image consisting of 4 copies of photo arranged
       in a 2x2 grid, with the top right, bottom left, and bottom
       right copies modified using filters CONTOUR, EMBOSS, and
       FIND_EDGES, respectively'''
    width, height = photo.size # width, height = size[0], size[1]

    # create new image big enough to contain 4 copies
    # of photo arranged in a 2x2 grid pattern
    res = PIL.Image.new(photo.mode, (2*width, 2*height))

    # put original photo in top left corner of res
    res.paste(photo, (0, 0, width, height))

    # put CONTOUR filtered image in top right corner of res
    contour = photo.filter(PIL.ImageFilter.CONTOUR)
    res.paste(contour, (width, 0, 2*width, height))

    # put EMBOSS filtered image in bottom left corner of res
    emboss = photo.filter(PIL.ImageFilter.EMBOSS)
    res.paste(emboss, (0, height, width, 2*height))

    # put FIND_EDGES filtered image in bottom right corner of res
    edges = photo.filter(PIL.ImageFilter.FIND_EDGES)
    res.paste(edges, (width, height, 2*width, 2*height))

    return res
