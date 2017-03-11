def dirContents(sPath):
    #prints contents of sPath
    import os
    print os.listdir(sPath)
    for cPath in os.listdir(sPath):
        childPath = os.path.join(sPath, cPath)
        if os.path.isdir(childPath):
            print 'dir: ', childPath
            print dirContents(childPath)
        else:
            print childPath

print dirContents('/Users/danielnilsson-cole/Desktop/python/projects/osTut')
