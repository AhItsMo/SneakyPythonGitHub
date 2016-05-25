@DeleteRepo
Feature: Delete an existing repository
    GitHub gives the user the ability to delete existing repositories.
    We need to make sure that a repository can be deleted when the user desires to.
    Also, the user should verify the name of the repository being deleted

    Scenario: Successful repository deletion
        Given Repository Settings page is displayed
        When the user attempts to delete this repository
        And the user verifies the name of the repository being deleted
        Then the repository is deleted successfully
