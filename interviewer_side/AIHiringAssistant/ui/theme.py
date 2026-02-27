from PyQt6.QtGui import QColor, QFont

class Theme:
    # --- PRO COLOR PALETTE (Slate & Blue) ---
    COLOR_BG = "#f8fafc"       # Slate 50
    COLOR_SURFACE = "#ffffff"  # White
    COLOR_PRIMARY = "#2563eb"  # Blue 600
    COLOR_PRIMARY_HOVER = "#1d4ed8" # Blue 700
    COLOR_ACCENT = "#00f0ff"   # Cyan (kept for specific highlights if needed)
    COLOR_TEXT_MAIN = "#0f172a" # Slate 900
    COLOR_TEXT_SEC = "#64748b"  # Slate 500
    COLOR_BORDER = "#e2e8f0"    # Slate 200
    
    # Status Colors
    COLOR_SUCCESS = "#16a34a"   # Green 600
    COLOR_WARNING = "#f59e0b"   # Amber 500
    COLOR_DANGER = "#ef4444"    # Red 500
    COLOR_SUCCESS_BG = "#dcfce7" # Green 100
    COLOR_WARNING_BG = "#fef3c7" # Amber 100
    COLOR_DANGER_BG = "#fee2e2"  # Red 100

    # --- TYPOGRAPHY ---
    FONT_FAMILY = "Segoe UI"
    
    @staticmethod
    def get_font(size=14, weight="normal"):
        return f"font-family: '{Theme.FONT_FAMILY}'; font-size: {size}px; font-weight: {weight};"

    # --- COMPONENT STYLES ---
    
    @staticmethod
    def global_style():
        return f"""
            QWidget {{
                background-color: {Theme.COLOR_BG};
                color: {Theme.COLOR_TEXT_MAIN};
                font-family: '{Theme.FONT_FAMILY}', sans-serif;
            }}
            QLabel {{
                color: {Theme.COLOR_TEXT_MAIN};
            }}
            QListWidget {{
                background-color: {Theme.COLOR_SURFACE};
                border: 1px solid {Theme.COLOR_BORDER};
                border-radius: 8px;
                padding: 10px;
            }}
        """

    @staticmethod
    def button_primary():
        return f"""
            QPushButton {{
                background-color: {Theme.COLOR_PRIMARY};
                color: white;
                font-size: 15px;
                font-weight: 600;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
            }}
            QPushButton:hover {{
                background-color: {Theme.COLOR_PRIMARY_HOVER};
            }}
            QPushButton:pressed {{
                background-color: #1e40af;
            }}
            QPushButton:disabled {{
                background-color: #cbd5e1;
                color: #94a3b8;
            }}
        """
        
    @staticmethod
    def button_secondary():
        return f"""
            QPushButton {{
                background-color: {Theme.COLOR_SURFACE};
                color: {Theme.COLOR_TEXT_SEC};
                font-size: 13px;
                border: 1px solid {Theme.COLOR_BORDER};
                border-radius: 6px;
                padding: 8px 16px;
            }}
            QPushButton:hover {{
                background-color: {Theme.COLOR_BG};
                color: {Theme.COLOR_TEXT_MAIN};
                border-color: #94a3b8;
            }}
        """

    @staticmethod
    def button_danger():
        return f"""
            QPushButton {{
                background-color: {Theme.COLOR_DANGER};
                color: white;
                font-size: 14px;
                font-weight: 600;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
            }}
            QPushButton:hover {{
                background-color: #dc2626;
            }}
        """

    @staticmethod
    def card_style():
        return f"""
            background-color: {Theme.COLOR_SURFACE};
            border: 1px solid {Theme.COLOR_BORDER};
            border-radius: 12px;
        """

    @staticmethod
    def input_style():
        return f"""
            QLineEdit {{
                background-color: {Theme.COLOR_SURFACE};
                border: 1px solid {Theme.COLOR_BORDER};
                border-radius: 6px;
                padding: 8px;
                color: {Theme.COLOR_TEXT_MAIN};
            }}
            QLineEdit:focus {{
                border: 2px solid {Theme.COLOR_PRIMARY};
            }}
        """
