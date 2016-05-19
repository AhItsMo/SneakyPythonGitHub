Feature: Create a new repository
    GitHub gives the user the ability to create no repositories.
    We need to make sure that a repository can be created easily without a problem,
    Unless the specified repository name is already taken.

    Scenario: Unsuccessful repository creation
        Given a repository is being created
        When the user attempts to use an unavailable repository name
        Then the repository already exists error message appears

    @wip
    Scenario: Successful repository creation
        Given a repository is being created
        When the user attempts to use an available repository name
        Then the repository is created successfully