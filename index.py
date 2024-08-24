class ExpertSinta:
    def __init__(self):
        self.facts = {
            "user_registered_as_expert": False,
            "credentials_verified": False,
            "is_expert": False,
            "expert_available": False,
            "session_scheduled": False,
            "payment_confirmed": False,
            "session_completed": False,
            "feedback_provided": False,
            "is_recommended_expert": False
        }
        self.rules = {
            "R1": self.apply_rule_1,
            "R2": self.apply_rule_2,
            "R3": self.apply_rule_3,
            "R4": self.apply_rule_4,
            "R5": self.apply_rule_5,
            "R6": self.apply_rule_6,
            "R7": self.apply_rule_7,
            "R8": self.apply_rule_8,
            "R9": self.apply_rule_9,
            "R10": self.apply_rule_10
        }

    def apply_rule_1(self):
        if self.facts["user_registered_as_expert"] and self.facts["credentials_verified"]:
            self.facts["is_expert"] = True

    def apply_rule_2(self):
        if self.facts["is_expert"]:
            self.facts["expert_available"] = True

    def apply_rule_3(self):
        if self.facts["expert_available"]:
            self.facts["session_scheduled"] = True

    def apply_rule_4(self):
        if self.facts["session_scheduled"]:
            self.facts["payment_confirmed"] = True

    def apply_rule_5(self):
        if self.facts["payment_confirmed"]:
            self.facts["session_completed"] = True

    def apply_rule_6(self):
        if self.facts["session_completed"]:
            self.facts["feedback_provided"] = True

    def apply_rule_7(self):
        if self.facts["feedback_provided"]:
            self.facts["is_recommended_expert"] = True

    def apply_rule_8(self):
        if not self.facts["session_scheduled"]:
            print("Expert's visibility may be reduced due to lack of scheduling.")

    def apply_rule_9(self):
        if self.facts["session_scheduled"] and not self.facts["payment_confirmed"]:
            self.facts["session_scheduled"] = False
            print("Session was canceled due to payment not being confirmed.")

    def apply_rule_10(self):
        if self.facts["is_recommended_expert"]:
            print("Expert is highlighted on the homepage.")

    def backward_chaining(self, goal):
        for rule_func in self.rules.values():
            rule_func()
        return self.facts.get(goal, False)


# Example usage of the ExpertSinta system
system = ExpertSinta()

# Setting initial facts
system.facts["user_registered_as_expert"] = True
system.facts["credentials_verified"] = True

# Checking if the expert became recommended
system.backward_chaining("is_recommended_expert")

# Printing the final state of the facts
print(system.facts)
