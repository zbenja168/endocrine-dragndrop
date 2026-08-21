BRICK = {
    "brick_num": 29,
    "brick_title": "Diabetic Ketoacidosis (DKA) and Hyperosmolar Hyperglycemic State (HHS)",
    "games": [
        {
            "slug": "dka_vs_hhs_clinical",
            "title": "DKA vs HHS at the Bedside",
            "subtitle": "Sort each clinical feature into the hyperglycemic emergency it characterizes",
            "categories": ["Usual diabetes type", "Speed of onset", "Ketone production", "Respiratory findings", "Neurologic findings", "Typical fluid deficit"],
            "data": {
                "Diabetic ketoacidosis (DKA)": {
                    "Usual diabetes type": "Type 1 diabetes, including new-onset or missed insulin doses",
                    "Speed of onset": "Rapid, over hours to about a day",
                    "Ketone production": "Unrestrained lipolysis makes acetoacetate and beta-hydroxybutyrate",
                    "Respiratory findings": "Kussmaul respirations with fruity, acetone-like breath odor",
                    "Neurologic findings": "Altered consciousness less common and usually milder",
                    "Typical fluid deficit": "Roughly 3-6 L from a shorter period of osmotic losses"
                },
                "Hyperosmolar hyperglycemic state (HHS)": {
                    "Usual diabetes type": "Type 2 diabetes, often with impaired thirst or limited water access",
                    "Speed of onset": "Insidious, evolving over days to weeks",
                    "Ketone production": "Residual insulin suppresses lipolysis, so ketogenesis stays minimal",
                    "Respiratory findings": "No compensatory hyperpnea, since significant acidosis does not develop",
                    "Neurologic findings": "Lethargy, stupor, coma, focal deficits, or seizures",
                    "Typical fluid deficit": "Roughly 8-12 L from prolonged osmotic diuresis"
                }
            }
        },
        {
            "slug": "diagnostic_lab_criteria",
            "title": "Diagnostic Labs: DKA, HHS, and Why",
            "subtitle": "Match each laboratory parameter to its DKA value, its HHS value, and the reason the two differ",
            "categories": ["Value in DKA", "Value in HHS", "Reason for the difference"],
            "data": {
                "Blood glucose": {
                    "Value in DKA": "Greater than 250 mg/dL, usually in the 250-600 range",
                    "Value in HHS": "Greater than 600 mg/dL, sometimes exceeding 1000 mg/dL",
                    "Reason for the difference": "HHS builds over weeks, so glucose climbs far higher before presentation"
                },
                "Arterial pH": {
                    "Value in DKA": "Less than 7.3, often falling below 7.1",
                    "Value in HHS": "Greater than 7.3, essentially preserved",
                    "Reason for the difference": "Only DKA generates enough ketoacid to overwhelm buffering capacity"
                },
                "Serum bicarbonate": {
                    "Value in DKA": "Less than 18 mEq/L",
                    "Value in HHS": "Greater than 18 mEq/L",
                    "Reason for the difference": "Bicarbonate buffer is consumed titrating circulating ketoacids"
                },
                "Serum ketones": {
                    "Value in DKA": "Positive at moderate to large levels",
                    "Value in HHS": "Absent or only trace",
                    "Reason for the difference": "Residual insulin in HHS blocks lipolysis and hepatic ketogenesis"
                },
                "Effective serum osmolality": {
                    "Value in DKA": "Variable, often under 320 mOsm/kg",
                    "Value in HHS": "Greater than 320 mOsm/kg",
                    "Reason for the difference": "Extreme glucose plus profound dehydration raise tonicity in HHS"
                },
                "Anion gap": {
                    "Value in DKA": "Elevated, above 12 mEq/L and often over 16",
                    "Value in HHS": "Normal or only mildly elevated",
                    "Reason for the difference": "Unmeasured ketoanions widen the gap only when ketosis is heavy"
                }
            }
        },
        {
            "slug": "potassium_guided_therapy",
            "title": "Potassium Decides When Insulin Starts",
            "subtitle": "Sort each management decision under the presenting serum potassium that dictates it",
            "categories": ["Insulin decision", "Potassium decision", "What the value reflects", "Main hazard if mishandled"],
            "data": {
                "Potassium below 3.5 mEq/L": {
                    "Insulin decision": "Hold the insulin infusion temporarily",
                    "Potassium decision": "Replace potassium first, before any insulin is given",
                    "What the value reflects": "Total-body depletion already showing up in the serum",
                    "Main hazard if mishandled": "Life-threatening hypokalemia and arrhythmia if insulin goes first"
                },
                "Potassium 3.5-5.5 mEq/L": {
                    "Insulin decision": "Start the insulin infusion now",
                    "Potassium decision": "Give potassium replacement as needed during therapy",
                    "What the value reflects": "Reassuring number that still masks a large total-body deficit",
                    "Main hazard if mishandled": "Potassium falling out of range as insulin takes effect"
                },
                "Potassium above 5.5 mEq/L": {
                    "Insulin decision": "Start insulin, which will help drive potassium into cells",
                    "Potassium decision": "Withhold potassium initially and recheck frequently",
                    "What the value reflects": "Extracellular shift from absent insulin and acidemia",
                    "Main hazard if mishandled": "Worsening hyperkalemia if supplementation is added too early"
                }
            }
        },
        {
            "slug": "treatment_framework",
            "title": "Treating DKA and HHS",
            "subtitle": "Match each intervention to its role in DKA, its role in HHS, and the pitfall it carries",
            "categories": ["Role in DKA", "Role in HHS", "Pitfall to avoid"],
            "data": {
                "Isotonic IV crystalloid": {
                    "Role in DKA": "First step; supports perfusion while insulin clears ketones",
                    "Role in HHS": "First and most urgent step; alone it substantially lowers glucose",
                    "Pitfall to avoid": "Correcting osmolality too fast invites neurologic complications"
                },
                "IV insulin infusion": {
                    "Role in DKA": "Central therapy, continued until ketosis and acidosis resolve",
                    "Role in HHS": "Secondary to fluids; lower dose after initial resuscitation",
                    "Pitfall to avoid": "Starting it before potassium is confirmed safe"
                },
                "Dextrose added to the fluids": {
                    "Role in DKA": "Added once glucose falls to about 200-250 mg/dL",
                    "Role in HHS": "Less pivotal, since rehydration itself drives glucose down",
                    "Pitfall to avoid": "Stopping insulin at that point instead of covering it with sugar"
                },
                "Potassium replacement": {
                    "Role in DKA": "Frequently required, since total-body potassium is depleted",
                    "Role in HHS": "Also required, with vigilant monitoring throughout treatment",
                    "Pitfall to avoid": "Trusting a normal serum level as evidence of normal stores"
                },
                "IV sodium bicarbonate": {
                    "Role in DKA": "Generally avoided; reserved for extreme acidemia",
                    "Role in HHS": "Not applicable, as significant acidosis does not develop",
                    "Pitfall to avoid": "Routine use, which can drive potassium even lower"
                },
                "Transition to subcutaneous insulin": {
                    "Role in DKA": "Only after ketosis and acidosis have fully resolved",
                    "Role in HHS": "Only after osmolality, volume, and mental status improve",
                    "Pitfall to avoid": "Any gap in coverage, given the 3-5 minute IV insulin half-life"
                }
            }
        }
    ]
}
