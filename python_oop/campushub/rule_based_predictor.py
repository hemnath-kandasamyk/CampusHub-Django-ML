from .predictor import PerformancePredictor


class RuleBasedPredictor(PerformancePredictor):

    def predict(self, attendance, marks):

        if attendance >= 75 and marks >= 60:
            return "GOOD"

        elif attendance >= 60 and marks >= 40:
            return "AVERAGE"

        return "AT RISK"

    def explain(self):
        return "Prediction is based on attendance and academic marks."