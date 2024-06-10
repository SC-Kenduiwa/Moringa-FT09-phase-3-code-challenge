class Author:
    def __init__(self, name):
        # Initialize author with validated name and empty articles list
        self._name = self._validate_name(name)
        self._articles = []

    @property
    def name(self):
        # Getter for the author's name
        return self._name

    def articles(self):
        # Return the list of articles written by the author
        return self._articles

    def topic_areas(self):
        # Return a list of unique topic areas based on the categories of the magazines
        return list(set(article.magazine.category for article in self._articles))

    def add_article(self, article):
        # Add an article to the author's list of articles
        self._articles.append(article)

    def _validate_name(self, name):
        # Validate the name to ensure it's a non-empty string
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        return name


class Magazine:
    def __init__(self, name, category):
        # Initialize magazine with validated name and category
        self._name = self._validate_name(name)
        self._category = self._validate_category(category)

    @property
    def name(self):
        # Getter for the magazine's name
        return self._name

    @property
    def category(self):
        # Getter for the magazine's category
        return self._category

    def _validate_name(self, name):
        # Validate the name to ensure it's a string between 2 and 16 characters
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        return name

    def _validate_category(self, category):
        # Validate the category to ensure it's a non-empty string
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category must be a non-empty string.")
        return category


class Article:
    def __init__(self, author, magazine, title):
        # Initialize article with author, magazine, and title, and add the article to the author's list
        self._author = author
        self._magazine = magazine
        self._title = self._validate_title(title)
        author.add_article(self)

    @property
    def title(self):
        # Getter for the article's title
        return self._title

    @property
    def author(self):
        # Getter for the article's author
        return self._author

    @property
    def magazine(self):
        # Getter for the article's magazine
        return self._magazine

    def _validate_title(self, title):
        # Validate the title to ensure it's a non-empty string
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")
        return title


def test_author():
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    magazine1 = Magazine("Tech Monthly", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    article1 = Article(author1, magazine1, "The Future of Tech")
    article2 = Article(author1, magazine2, "AI in Healthcare")

    assert len(author1.articles()) == 2
    assert set(author1.topic_areas()) == {"Technology", "Health"}


def test_magazine():
    magazine1 = Magazine("Tech Monthly", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")

    assert magazine1.name == "Tech Monthly"
    assert magazine1.category == "Technology"


def test_article():
    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Monthly", "Technology")

    article1 = Article(author1, magazine1, "The Future of Tech")

    assert article1.title == "The Future of Tech"
    assert article1.author == author1
    assert article1.magazine == magazine1


if __name__ == "__main__":
    test_author()
    test_magazine()
    test_article()
    print("All tests passed!")
