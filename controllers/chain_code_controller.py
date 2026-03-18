from core.chain_code import get_chain_code


class ChainCodeController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.final_points = None

        self.main_window.btnCalcChainCode.setEnabled(False)
        self.main_window.btnCalcChainCode.clicked.connect(self.calculate_chain_code)

    def set_final_points(self, final_points):
        self.final_points = final_points
        self.main_window.btnCalcChainCode.setEnabled(True)

    def reset(self):
        self.final_points = None
        self.main_window.btnCalcChainCode.setEnabled(False)
        self.main_window.txtChainCodeResult.clear()

    def calculate_chain_code(self):
        if self.final_points is None:
            return

        contour_points_count = len(self.final_points)
        chain_code = get_chain_code(self.final_points)
        chain_code_count = len(chain_code)

        # print(f"Contour points count: {contour_points_count}")
        # print(f"Chain code count: {chain_code_count}")

        chain_code_text = " ".join(map(str, chain_code))
        self.main_window.txtChainCodeResult.setPlainText(chain_code_text)
