from abc import ABCMeta, abstractmethod


class NewsPublisher:
    """
        This is a subject class.
    """
    def __int__(self):
        self.__subscriber = []
        self.__latest_news = None

    def attach(self, subscriber):
        self.__subscriber.append(subscriber)

    def detach(self):
        return self.__subscriber.pop()

    def subscribers_list(self):
        return [type(x).__name__ for x in self.__subscriber]

    def notify_subscribers(self):
        for sub in self.__subscriber:
            sub.update()

    def add_news(self, news):
        self.__latestNews = news

    def get_news(self):
        return "Got News:", self.__latestNews


class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber:
    """
        This is a ConcreteObserver class.
    """
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber:
    """
        This is a ConcreteObserver class.
    """
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    news_publisher = NewsPublisher()

    for subscribers in [SMSSubscriber, EmailSubscriber]:
        subscribers(news_publisher)
    print("\nSubscribers:", news_publisher.subscribers_list())

    news_publisher.add_news('Hello World!')
    news_publisher.notify_subscribers()
    print("\nDetached:", type(news_publisher.detach()).__name__)
    print("\nSubscribers:", news_publisher.subscribers_list())
    news_publisher.add_news('My second news!')
    news_publisher.notify_subscribers()

