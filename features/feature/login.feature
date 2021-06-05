Feature: Login

   @login
   Scenario Outline: Log in to Gmail
      # Given I am on the login docs page with username "<username>" and password "<password>"
      When I click on add on
      Then I click on Actable AI
      Then I click on Regression
      Then I switch to iframe
      Then I select to predicted target and valuePredictedTarget "<valuePredictedTarget>"
      Then I click on select rendered
      Then I click on select all value
      Then I select to predicted target and valuePredictedTarget "<valuePredictedTarget>"
      Then I click on run button
      Then I quit iframe
      Then I check to exist regression validation sheet
      Then I right click on regression validation sheet to delete
      Then I click on delete button
      Then I click on OK button to confirm
      Examples:
         | username | password | valuePredictedTarget |
         | username | password | rental_price         |

# @login
# Scenario: Log in to Gmail
#    Given I am on the login page and input username and password
#    #  When I enter the link docs google
#    #  Then the user is logged in

