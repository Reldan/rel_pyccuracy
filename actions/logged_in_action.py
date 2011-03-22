from pyccuracy.actions import ActionBase
from pyccuracy.errors import ActionFailedError

class LoggedInAction(ActionBase):
    regex = r'^(And )?I am logged in with username [\"](?P<username>.+)[\"] and password [\"](?P<password>.+)[\"]$'

    def execute(self, context, username, password):
        self.execute_action(u"I go to \"/index.html\"", context)

        # if the user is not logged in already, we do the login process
        logged_in = False
        try:
            self.execute_action(u"And I see \"already have an account? sign in\" link", context)
        except ActionFailedError:
            logged_in = True

        if not logged_in:
            self.execute_action(u"And I click \"already have an account? sign in\" link", context)
            self.execute_action(u"And I wait for the page to load for 5 seconds", context)
            self.execute_action(u"And I fill \"username\" textbox with \"%s\"" % username, context)
            self.execute_action(u"And I fill \"password\" textbox with \"%s\"" % password, context)
            self.execute_action(u"And I click \"sign in\" button", context)