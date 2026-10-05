import customtkinter as ctk
from tkinter import messagebox

from calculation_service import CalculationService
from models import (
    CalculationRequest,
    ConnectionType,
)
from storage import CalculationStorage


class PowerCalculatorGUI:
    def __init__(self, root):
        self.root = root

        self.root.title(
            "Three-Phase Power Calculator"
        )

        self.root.geometry(
            "900x620"
        )

        self.root.minsize(
            850,
            580,
        )

        self.service = CalculationService()
        self.storage = CalculationStorage()

        self.connection_type = ctk.StringVar(
            value=ConnectionType.WYE.value
        )

        self.voltage_var = ctk.StringVar()
        self.current_var = ctk.StringVar()
        self.power_factor_var = ctk.StringVar()

        self.build_interface()

    def build_interface(self):
        self.root.grid_columnconfigure(
            0,
            weight=1,
        )

        self.root.grid_rowconfigure(
            0,
            weight=1,
        )

        main = ctk.CTkFrame(
            self.root,
            fg_color="transparent",
        )

        main.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=30,
            pady=25,
        )

        main.grid_columnconfigure(
            0,
            weight=1,
        )

        main.grid_columnconfigure(
            1,
            weight=1,
        )

        main.grid_rowconfigure(
            1,
            weight=1,
        )

        # HEADER

        header = ctk.CTkFrame(
            main,
            fg_color="transparent",
        )

        header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 20),
        )

        ctk.CTkLabel(
            header,
            text="Three-Phase Power Calculator",
            font=ctk.CTkFont(
                size=28,
                weight="bold",
            ),
        ).pack(anchor="w")

        ctk.CTkLabel(
            header,
            text=(
                "Balanced three-phase power calculation"
            ),
            text_color=("gray45", "gray65"),
        ).pack(
            anchor="w",
            pady=(3, 0),
        )

        # INPUT CARD

        input_card = ctk.CTkFrame(
            main,
            corner_radius=16,
        )

        input_card.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(0, 10),
        )

        input_card.grid_columnconfigure(
            0,
            weight=1,
        )

        ctk.CTkLabel(
            input_card,
            text="Calculation Inputs",
            font=ctk.CTkFont(
                size=19,
                weight="bold",
            ),
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=22,
            pady=(22, 18),
        )

        ctk.CTkLabel(
            input_card,
            text="Connection Type",
            font=ctk.CTkFont(
                weight="bold",
            ),
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=22,
            pady=(0, 6),
        )

        self.connection_selector = (
            ctk.CTkSegmentedButton(
                input_card,
                values=[
                    ConnectionType.WYE.value,
                    ConnectionType.DELTA.value,
                ],
                variable=self.connection_type,
            )
        )

        self.connection_selector.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=22,
            pady=(0, 16),
        )

        self.add_input(
            input_card,
            row=3,
            label="Line Voltage (V)",
            variable=self.voltage_var,
        )

        self.add_input(
            input_card,
            row=4,
            label="Line Current (A)",
            variable=self.current_var,
        )

        self.add_input(
            input_card,
            row=5,
            label="Power Factor",
            variable=self.power_factor_var,
        )

        button_frame = ctk.CTkFrame(
            input_card,
            fg_color="transparent",
        )

        button_frame.grid(
            row=6,
            column=0,
            sticky="ew",
            padx=22,
            pady=(10, 22),
        )

        button_frame.grid_columnconfigure(
            0,
            weight=1,
        )

        button_frame.grid_columnconfigure(
            1,
            weight=1,
        )

        ctk.CTkButton(
            button_frame,
            text="Calculate",
            command=self.calculate,
            height=42,
            font=ctk.CTkFont(
                weight="bold",
            ),
        ).grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 5),
        )

        ctk.CTkButton(
            button_frame,
            text="Clear",
            command=self.clear,
            height=42,
            fg_color=("gray75", "gray28"),
            hover_color=("gray65", "gray35"),
            text_color=("gray10", "gray95"),
        ).grid(
            row=0,
            column=1,
            sticky="ew",
            padx=(5, 0),
        )

        # RESULT CARD

        result_card = ctk.CTkFrame(
            main,
            corner_radius=16,
        )

        result_card.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(10, 0),
        )

        result_card.grid_columnconfigure(
            0,
            weight=1,
        )

        result_card.grid_rowconfigure(
            2,
            weight=1,
        )

        ctk.CTkLabel(
            result_card,
            text="Results",
            font=ctk.CTkFont(
                size=19,
                weight="bold",
            ),
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=22,
            pady=(22, 5),
        )

        self.primary_result = ctk.CTkLabel(
            result_card,
            text="Ready",
            font=ctk.CTkFont(
                size=28,
                weight="bold",
            ),
        )

        self.primary_result.grid(
            row=1,
            column=0,
            sticky="w",
            padx=22,
            pady=(5, 15),
        )

        self.result_text = ctk.CTkTextbox(
            result_card,
            font=ctk.CTkFont(
                family="Consolas",
                size=13,
            ),
        )

        self.result_text.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=22,
            pady=(0, 15),
        )

        self.result_text.configure(
            state="disabled"
        )

        self.status_label = ctk.CTkLabel(
            result_card,
            text="Ready for a calculation",
            height=34,
            corner_radius=8,
            fg_color=("gray88", "gray24"),
        )

        self.status_label.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=22,
            pady=(0, 22),
        )

        self.root.bind(
            "<Return>",
            lambda event: self.calculate(),
        )

    def add_input(
        self,
        parent,
        row,
        label,
        variable,
    ):
        frame = ctk.CTkFrame(
            parent,
            fg_color="transparent",
        )

        frame.grid(
            row=row,
            column=0,
            sticky="ew",
            padx=22,
            pady=(0, 14),
        )

        frame.grid_columnconfigure(
            0,
            weight=1,
        )

        ctk.CTkLabel(
            frame,
            text=label,
            font=ctk.CTkFont(
                weight="bold",
            ),
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 5),
        )

        ctk.CTkEntry(
            frame,
            textvariable=variable,
            height=38,
        ).grid(
            row=1,
            column=0,
            sticky="ew",
        )

    @staticmethod
    def parse_number(
        value,
        field_name,
    ):
        value = value.strip()

        if not value:
            raise ValueError(
                f"{field_name} is required."
            )

        try:
            return float(value)

        except ValueError:
            raise ValueError(
                f"{field_name} must be numeric."
            )

    def calculate(self):
        try:
            voltage = self.parse_number(
                self.voltage_var.get(),
                "Line voltage",
            )

            current = self.parse_number(
                self.current_var.get(),
                "Line current",
            )

            power_factor = self.parse_number(
                self.power_factor_var.get(),
                "Power factor",
            )

            request = CalculationRequest(
                connection_type=ConnectionType(
                    self.connection_type.get()
                ),
                line_voltage=voltage,
                line_current=current,
                power_factor=power_factor,
            )

            result = self.service.calculate(
                request
            )

            # Real storage write.
            self.storage.save(
                result
            )

            # Read the same result back from
            # persistent storage before display.
            saved_result = (
                self.storage.load_latest()
            )

            self.display_result(
                saved_result
            )

            self.status_label.configure(
                text=(
                    "✓ Result saved and loaded "
                    "from storage"
                ),
                fg_color=(
                    "#d9f2e3",
                    "#173b2b",
                ),
                text_color=(
                    "#166534",
                    "#86efac",
                ),
            )

        except ValueError as error:
            self.status_label.configure(
                text="Calculation failed"
            )

            messagebox.showerror(
                "Invalid Input",
                str(error),
            )

    def display_result(
        self,
        result,
    ):
        self.primary_result.configure(
            text=(
                f"{result['real_power'] / 1000:.3f} kW"
            )
        )

        text = (
            f"Connection       "
            f"{result['connection_type']}\n"
            f"Line Voltage     "
            f"{result['line_voltage']:.2f} V\n"
            f"Phase Voltage    "
            f"{result['phase_voltage']:.2f} V\n"
            f"Line Current     "
            f"{result['line_current']:.2f} A\n"
            f"Phase Current    "
            f"{result['phase_current']:.2f} A\n"
            f"Power Factor     "
            f"{result['power_factor']:.3f}\n\n"
            f"Apparent Power   "
            f"{result['apparent_power'] / 1000:.3f} kVA\n"
            f"Real Power       "
            f"{result['real_power'] / 1000:.3f} kW\n"
            f"Reactive Power   "
            f"{result['reactive_power'] / 1000:.3f} kVAR"
        )

        self.result_text.configure(
            state="normal"
        )

        self.result_text.delete(
            "1.0",
            "end",
        )

        self.result_text.insert(
            "end",
            text,
        )

        self.result_text.configure(
            state="disabled"
        )

    def clear(self):
        self.voltage_var.set("")
        self.current_var.set("")
        self.power_factor_var.set("")

        self.primary_result.configure(
            text="Ready"
        )

        self.result_text.configure(
            state="normal"
        )

        self.result_text.delete(
            "1.0",
            "end",
        )

        self.result_text.configure(
            state="disabled"
        )

        self.status_label.configure(
            text="Ready for a calculation",
            fg_color=("gray88", "gray24"),
            text_color=("gray10", "gray90"),
        )