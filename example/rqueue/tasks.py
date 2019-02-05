from django_rq import job


@job
def count_chars(string):
    count = len(string)
    print(f"There are {count} characters in {string}")


@job
def count_words(string):
    count = len(string.split("\n"))
    print(f"There are {count} words in {string}")


@job
def idempotent_method():
    print(f"Minute scheduler has been triggered")


@job
def idempotent_method2():
    print(f"2 minute scheduler has been triggered")
