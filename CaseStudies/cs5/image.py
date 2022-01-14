def copy(original):
    'returns copy of image photo'

    # create a new image of the same mode and size as original
    res = PIL.Image.new(original.mode, original.size)
    # width = original.size[0], height = original.size[1]
    width, height = original.size

    # nested loop pattern to access individual pixels
    for i in range(0, width):
        for j in range(0, height):
            # set pix to color of pixel
            # at location (i,j) of original
            pix = original.getpixel((i,j))
            # set pixel at location (i,j) of res to pix
            res.putpixel((i,j), pix)
    return res


def rotateCC(original):
    'returns copy of photo rotated counterclockwise 90 degrees'

    # n and m are width and height, resp., of original
    n, m = original.size
    # m and n are width and height, resp., of new image
    res = PIL.Image.new(original.mode, (m,n))

    # nested loop pattern copies colors from original to res
    for i in range(0, n):
        for j in range(0, m):
            pixel = original.getpixel((i,j))
            # pixel at location (i,j) in original is
            # mapped to pixel at location (j,n-i-1) in res
            res.putpixel((j, n-i-1), pixel)
    return res




def smooth(original):
    'returns smooth copy of original'
    # new image has same mode and size as original
    res = PIL.Image.new(original.mode, original.size)    
    width, height = original.size

    # nested loop pattern computes the color of every pixel in res
    for i in range(0, width):
        for j in range(0, height):
            # initialize sums of colors red, green and blue
            red, green, blue = 0, 0, 0
            # initialize counter of neighbors of pixel (i, j)
            numPixels = 0
            # nested loop pattern generates locations
            # (c, r) of pixel (i, j) and its neighbors
            for c in range(max(0, i-1), min(width, i+2)):
                for r in range(max(0, j-1), min(height, j+2)):
                    # increment neighbor count
                    numPixels +=1
                    # add colors of pixel (c, r) to sums
                    # red, green, blue
                    pixel = original.getpixel((c, r))
                    red = red + pixel[0]
                    green = green + pixel[1]
                    blue = blue + pixel[2]
            # compute average of red, green, and blue colors
            red = red//numPixels
            green = green//numPixels
            blue = blue//numPixels
            # color pixel (i, j) of res with average color
            res.putpixel((i, j), (red, green, blue))
    return res



    
##################################
# Solutions to Practice Problems #
##################################


# Practice Problem CS.26
def crop(original, box):
    '''returns copy of image original cropped using
       the rectangular region defined by box'''
    # rows and colums that define region to be cropped
    x1,y1,x2,y2 = box
    # width and height of new image
    width,height = x2-x1, y2-y1
    # create new image to contain cropped image
    res = PIL.Image.new(original.mode, (width, height))
    # nested loop pattern copies pixel colors from original to res
    for i in range(width):
        for j in range(height):
            # set pix to color of pixel at location (x1+i,y1+j)
            # of original
            pix = original.getpixel((x1+i,y1+j))
            # set pixel at location (i,j) of res to pix
            res.putpixel((i,j), pix)
    return res


# Practice Problem CS.27
def rotateCL(original):
    'returns copy of original image rotated clockwise 90 degrees'

    # n and m are width and height, resp., of original
    n, m = original.size
    # m and n are width and height, resp., of new image
    res = PIL.Image.new(original.mode, (m,n))

    # nested loop pattern copies colors from original to res
    for i in range(0, n):
        for j in range(0, m):
            pixel = original.getpixel((i,j))
            # pixel at location (i,j) in original is
            # mapped to pixel at location (m-j-1,i) in res
            res.putpixel((m-j-1, i), pixel)
    return res
