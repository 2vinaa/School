from School.Prog.LabTest.doubleLinkedList import DLinkedList

class ImageViewer:
    def __init__(self):
        self.currentImage = None
        self.imageList = DLinkedList()

    def add_image(self,filename):
        self.imageList.append(filename)
        if self.currentImage is None:
            self.currentImage = self.imageList.head


    def next_image(self):
        if self.currentImage is not None and self.currentImage.next is not None:
            self.currentImage = self.currentImage.next
            return self.currentImage.data
        else:
            print("No next image")

    def previous_image(self):
        if self.currentImage is not None and self.currentImage.prev is not None:
            self.currentImage = self.currentImage.prev
            return self.currentImage.data
        else:
            print("No previous image")


    def current_image(self):
        if self.currentImage is not None:
            return self.currentImage.data
        else:
            print("No current image")

if __name__ == "__main__":
    viewer = ImageViewer()
    viewer.add_image("img1.png")
    viewer.add_image("img2.png")
    viewer.add_image("img3.png")
    viewer.next_image()
    viewer.next_image()
    viewer.previous_image()
    print(viewer.current_image())  # img2.png