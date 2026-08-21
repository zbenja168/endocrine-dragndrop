BRICK = {
    "brick_num": 25,
    "brick_title": "Type 2 Diabetes Mellitus (T2D)",
    "games": [
        {
            "slug": "t1d_vs_t2d",
            "title": "Type 1 vs Type 2 Diabetes",
            "subtitle": "Sort each clinical or laboratory feature into the type of diabetes it points toward",
            "categories": ["Tempo of onset", "Body habitus", "C-peptide level", "Islet autoantibodies", "Characteristic acute crisis", "Skin and exam clues"],
            "data": {
                "Type 1 diabetes mellitus": {
                    "Tempo of onset": "Acute, symptomatic presentation over days to weeks",
                    "Body habitus": "Typically younger and leaner, often with weight loss",
                    "C-peptide level": "Low or undetectable from marked beta-cell loss",
                    "Islet autoantibodies": "GAD65, IA-2, ZnT8 present in most new-onset cases",
                    "Characteristic acute crisis": "Diabetic ketoacidosis from absent insulin secretion",
                    "Skin and exam clues": "Few insulin-resistance signs; dehydration and weight loss dominate"
                },
                "Type 2 diabetes mellitus": {
                    "Tempo of onset": "Gradual onset over years, often found incidentally on screening",
                    "Body habitus": "Obese with predominantly abdominal (visceral) fat",
                    "C-peptide level": "Normal or elevated, reflecting preserved beta-cell function",
                    "Islet autoantibodies": "Generally absent, supporting the diagnosis clinically",
                    "Characteristic acute crisis": "Hyperosmolar hyperglycemic state, since residual insulin blocks ketogenesis",
                    "Skin and exam clues": "Acanthosis nigricans, central obesity, hypertension, dyslipidemia"
                }
            }
        },
        {
            "slug": "insulin_resistance_tissues",
            "title": "Insulin Resistance, Tissue by Tissue",
            "subtitle": "Match each tissue to insulin's normal job there, the defect in T2D, and the metabolic result",
            "categories": ["Normal insulin action", "Defect in T2D", "Metabolic consequence"],
            "data": {
                "Skeletal muscle": {
                    "Normal insulin action": "Insulin triggers GLUT4 translocation to the cell surface",
                    "Defect in T2D": "GLUT4 translocation is impaired despite insulin signal",
                    "Metabolic consequence": "Body's major site of glucose disposal fails to clear glucose"
                },
                "Adipose tissue": {
                    "Normal insulin action": "Insulin drives glucose uptake and restrains lipolysis",
                    "Defect in T2D": "Adipocytes resist insulin's antilipolytic effect",
                    "Metabolic consequence": "Excess free fatty acids worsen resistance in liver and muscle"
                },
                "Liver": {
                    "Normal insulin action": "Insulin suppresses gluconeogenesis and glycogenolysis",
                    "Defect in T2D": "Suppression of hepatic glucose production is blunted",
                    "Metabolic consequence": "Active glucose overproduction drives fasting hyperglycemia"
                },
                "Pancreatic beta cell": {
                    "Normal insulin action": "Secretes insulin in proportion to the metabolic demand",
                    "Defect in T2D": "Compensatory hypersecretion later fails from gluco- and lipotoxicity",
                    "Metabolic consequence": "Insulin secretion becomes inadequate and glucose reaches diabetic range"
                },
                "Pancreatic alpha cell": {
                    "Normal insulin action": "Insulin suppresses glucagon release after a meal",
                    "Defect in T2D": "Paracrine suppression of glucagon is impaired",
                    "Metabolic consequence": "Inappropriately high glucagon further raises hepatic glucose output"
                }
            }
        },
        {
            "slug": "ada_diagnostic_criteria",
            "title": "ADA Diagnostic Criteria for Diabetes",
            "subtitle": "Match each diagnostic test to its threshold, its conditions of use, and what it measures",
            "categories": ["Diagnostic threshold", "Condition or caveat", "What it measures"],
            "data": {
                "Fasting plasma glucose": {
                    "Diagnostic threshold": "126 mg/dL (7.0 mmol/L) or higher",
                    "Condition or caveat": "Requires no caloric intake for at least 8 hours",
                    "What it measures": "Plasma glucose in the fasted state"
                },
                "Hemoglobin A1c": {
                    "Diagnostic threshold": "6.5% or higher",
                    "Condition or caveat": "Standardized assay required; a value below 6.5% does not exclude T1D",
                    "What it measures": "Glycated hemoglobin as a fraction of total hemoglobin over ~2-3 months"
                },
                "Random plasma glucose": {
                    "Diagnostic threshold": "200 mg/dL (11.1 mmol/L) or higher",
                    "Condition or caveat": "Used only in patients showing symptoms of hyperglycemia",
                    "What it measures": "Plasma glucose at any time of day, regardless of meals"
                },
                "2-hour oral glucose tolerance test": {
                    "Diagnostic threshold": "200 mg/dL (11.1 mmol/L) or higher at 2 hours",
                    "Condition or caveat": "Valid but not frequently used in current practice",
                    "What it measures": "Plasma glucose 2 hours after ingesting a glucose load"
                }
            }
        },
        {
            "slug": "presentation_clues",
            "title": "Clues at Presentation",
            "subtitle": "Match each finding to where it shows up, its mechanism, and the clinical message it carries",
            "categories": ["Where it shows up", "Mechanism", "Clinical message"],
            "data": {
                "Acanthosis nigricans": {
                    "Where it shows up": "Skin folds of the neck, axillae, and groin",
                    "Mechanism": "Cutaneous signal of underlying insulin resistance",
                    "Clinical message": "Velvety discoloration that does not wash off with vigorous cleaning"
                },
                "Central obesity": {
                    "Where it shows up": "Visceral, intra-abdominal fat compartment",
                    "Mechanism": "Visceral adiposity is a hallmark driver of insulin resistance",
                    "Clinical message": "Captured best by waist circumference or waist-to-hip ratio, not BMI"
                },
                "Polyuria and polydipsia": {
                    "Where it shows up": "Urine output and fluid intake",
                    "Mechanism": "Osmotic diuresis from sustained hyperglycemia",
                    "Clinical message": "Often mild or absent early, because residual insulin blunts glucose rise"
                },
                "Polyphagia": {
                    "Where it shows up": "Appetite and eating behavior",
                    "Mechanism": "Cellular glucose deprivation despite high circulating glucose",
                    "Clinical message": "Completes the classic triad of the 3 P's"
                },
                "Recurrent infections": {
                    "Where it shows up": "Urinary tract and skin",
                    "Mechanism": "Consequence of chronically elevated blood glucose",
                    "Clinical message": "Nonspecific complaint that should still prompt glycemic testing"
                },
                "Tingling and numbness": {
                    "Where it shows up": "Feet and distal lower extremities",
                    "Mechanism": "Peripheral neuropathy from long-standing unrecognized disease",
                    "Clinical message": "Suggests complications were already developing before diagnosis"
                }
            }
        }
    ]
}
