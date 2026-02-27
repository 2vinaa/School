
from multarr import Array
from doubleLinkedList import DLinkedList
from LinkedList import LinkedList


class HistoryNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None


class BookmarkNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.isBookMark = False


class BrowserHistory:
    def __init__(self):
        self.curr_tab = None
        self.b_history = DLinkedList()
        self.bookmark_bar = Array(6)
        for i in range(len(self.bookmark_bar)):
            self.bookmark_bar[i] = LinkedList()

    def _hash_function(self, url:str):
        x = 0
        for element in str(url):
            x += ord(element)
        return x % len(self.bookmark_bar)

    def visit(self, url):
        url_node = HistoryNode(url)
        if self.curr_tab is None:
            self.b_history.append(url_node)
            self.b_history.head = url_node
            self.b_history.tail = url_node
            self.curr_tab = url_node
        elif self.curr_tab is not None:
            self.curr_tab.next = url_node
            url_node.prev = self.curr_tab
            self.curr_tab = url_node
            self.b_history.tail = url_node
        self.curr_tab.next = None


    def bookmark(self):
        x = self._hash_function(self.curr_tab)
        if not self.bookmark_bar[x].search_linear(BookmarkNode(self.curr_tab)):
            self.bookmark_bar[x].append_linear(BookmarkNode(self.curr_tab))

    
    def is_bookmarked(self, url):
        x = self._hash_function(url)
        return self.bookmark_bar[x].search_linear(url) is not None

    def back(self, steps):
        if self.b_history.isEmpty():
            return "Cant take a step back on an empty list"
        else:
            while steps > 0:
                self.curr_tab = self.curr_tab.prev
                steps -= 1
            if self.curr_tab is None:
                return "You have taken too many steps back"
            else:
                return f"We know find ourselves at {self.curr_tab.url}"


    def forward(self, steps):
        if self.b_history.isEmpty():
            return "Cant take a step forward on an empty list"
        else:
            while steps > 0:
                self.curr_tab = self.curr_tab.next
                steps -= 1
            if self.curr_tab is None:
                return "You have taken too many steps forward"
            else:
                return f"We know find ourselves at {self.curr_tab.url}"

    def print_history(self):
        print_of_websites = []
        value = self.b_history.head
        while value is not None:
            if self.is_bookmarked(value.url):
                a = "*" + str(value.url)
                print_of_websites.append(a)
            else:
                print_of_websites.append(value.url)

            value = value.next

        for i in print_of_websites:
            print(i)
    
    def print_bookmarks(self):
        bookmark_list = []
        for i in self.bookmark_bar:

            value = i.head
            while value is not None:
                bookmark_list.append(value.url)
                value = value.next

        for element in bookmark_list:
            print(element.url)


if __name__=="__main__":
    # Tests: Check the tests before starting to code the assignments. 
    #        If the test are not clear, ask for clarifications.
    #
    browser = BrowserHistory()
    browser.visit("donotusechatgp.com")
    browser.visit("donotusegenerativetools.org")
    browser.visit("wearegoingtouseantiplagiarismtools.edu")
    browser.visit("supsi.ch")
    browser.bookmark()
    browser.visit("usi.ch")
    browser.visit("google.com")
    browser.bookmark()
    browser.visit("github.com")
    browser.visit("stackoverflow.com")
    browser.visit("python.org")
    browser.bookmark()
    browser.visit("w3schools.com")

    print("== Initial history:")
    browser.print_history()
    """
    == Initial history:
      donotusechatgp.com
      donotusegenerativetools.org
      wearegoingtouseantiplagiarismtools.edu
      * supsi.ch
      usi.ch
      * google.com
      github.com
      stackoverflow.com
      * python.org
    > w3schools.com
    """
    print(f"== Going back 2 steps to {browser.back(2)} and bookmark:")
    browser.bookmark()
    browser.print_history()
    """
    == Going back 2 steps to stackoverflow.com and bookmark:
      donotusechatgp.com
      donotusegenerativetools.org
      wearegoingtouseantiplagiarismtools.edu
      * supsi.ch
      usi.ch
      * google.com
      github.com
    > * stackoverflow.com
      * python.org
      w3schools.com
    """
    print(f"== Going forward 1 step to {browser.forward(1)}:")
    browser.print_history()
    """
    == Going forward 1 step to python.org:
      donotusechatgp.com
      donotusegenerativetools.org
      wearegoingtouseantiplagiarismtools.edu
      * supsi.ch
      usi.ch
      * google.com
      github.com
      * stackoverflow.com
    > * python.org
      w3schools.com
    """
    print(f"== Going back 2 steps to {browser.back(2)}:")
    browser.print_history()
    """
    == Going back 2 steps to github.com:
      donotusechatgp.com
      donotusegenerativetools.org
      wearegoingtouseantiplagiarismtools.edu
      * supsi.ch
      usi.ch
      * google.com
    > github.com
      * stackoverflow.com
      * python.org
      w3schools.com
    """
    print("== Visit webpage (it should remove the forward history)")
    browser.visit("bling.com")
    browser.print_history()
    """
    == Visit webpage (it should remove the forward history)
      donotusechatgp.com
      donotusegenerativetools.org
      wearegoingtouseantiplagiarismtools.edu
      * supsi.ch
      usi.ch
      * google.com
      github.com
    > bling.com
    """
    print("== Visit more webpages and bookmark")
    browser.visit("youtube.com")
    browser.visit("google.com")
    browser.visit("notion.so")
    browser.bookmark()
    browser.visit("android.com")
    browser.bookmark()
    browser.visit("apple.com")
    browser.visit("samsung.com")
    browser.visit("spotify.com")
    browser.bookmark()
    browser.visit("netflix.com")
    browser.bookmark()
    browser.visit("lightning.ai")
    browser.bookmark()
    browser.visit("colab.research.google.com")
    browser.visit("arxiv.org")
    browser.bookmark()
    browser.visit("developer.nvidia.com")
    browser.visit("nature.com")
    browser.bookmark()
    browser.visit("gitlab.com")
    browser.bookmark()
    browser.visit("aicrowd.com")
    browser.print_history()
    """
    == Visit more webpages and bookmark
      donotusechatgp.com
      donotusegenerativetools.org
      wearegoingtouseantiplagiarismtools.edu
      * supsi.ch
      usi.ch
      * google.com
      github.com
      bling.com
      youtube.com
      * google.com
      * notion.so
      * android.com
      apple.com
      samsung.com
      * spotify.com
      * netflix.com
      * lightning.ai
      colab.research.google.com
      * arxiv.org
      developer.nvidia.com
      * nature.com
      * gitlab.com
    > aicrowd.com
    """
    print(f"== Going back 5 steps to {browser.back(5)} and visiting:")
    browser.visit("nature.com")
    browser.print_history()
    """
    == Going back 5 steps to colab.research.google.com and visiting:
      donotusechatgp.com
      donotusegenerativetools.org
      wearegoingtouseantiplagiarismtools.edu
      * supsi.ch
      usi.ch
      * google.com
      github.com
      bling.com
      youtube.com
      * google.com
      * notion.so
      * android.com
      apple.com
      samsung.com
      * spotify.com
      * netflix.com
      * lightning.ai
      colab.research.google.com
    > * nature.com
    """
    print("** Bookmarked pages (the hashing list with 6 buckets)** ")
    browser.print_bookmarks()
    """
    ** Bookmarked pages (the hashing list with 6 buckets)** 
    Bucket 0: google.com -> lightning.ai -> nature.com -> None
    Bucket 1: stackoverflow.com -> spotify.com -> None
    Bucket 2: gitlab.com -> None
    Bucket 3: supsi.ch -> None
    Bucket 4: python.org -> android.com -> arxiv.org -> None
    Bucket 5: notion.so -> netflix.com -> None
    """
