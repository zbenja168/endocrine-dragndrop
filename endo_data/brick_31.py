BRICK = {
    "brick_num": 31,
    "brick_title": "Hypoglycemia",
    "games": [
        {
            "slug": "fasting_vs_reactive",
            "title": "Fasting vs Reactive Hypoglycemia",
            "subtitle": "Sort each feature into the pattern of hypoglycemia it belongs to",
            "categories": ["Fasting hypoglycemia", "Reactive hypoglycemia", "Idiopathic postprandial syndrome"],
            "data": {
                "Timing of symptoms": {
                    "Fasting hypoglycemia": "In the morning before eating, or during the day if a meal is missed",
                    "Reactive hypoglycemia": "After meals, typically 2 to 4 hours later",
                    "Idiopathic postprandial syndrome": "After meals, with the same jittery postprandial complaints"
                },
                "Glucose level during a spell": {
                    "Fasting hypoglycemia": "Often severely low, low enough to cause marked symptoms",
                    "Reactive hypoglycemia": "Low but seldom low enough to produce severe symptoms",
                    "Idiopathic postprandial syndrome": "No documented fall in blood glucose at all"
                },
                "Usual cause": {
                    "Fasting hypoglycemia": "Glucose-lowering drugs, low cortisol, or kidney or liver disease",
                    "Reactive hypoglycemia": "Upper GI surgery causing rapid glucose transit and an insulin surge",
                    "Idiopathic postprandial syndrome": "Unknown; no underlying disease is identified"
                },
                "Confirmatory test": {
                    "Fasting hypoglycemia": "Supervised 72-hour fast with glucose and insulin every 6 hours",
                    "Reactive hypoglycemia": "Supervised mixed meal test with hourly glucose for 5 hours",
                    "Idiopathic postprandial syndrome": "Testing shows symptoms while glucose stays above 55 mg/dL"
                },
                "Management": {
                    "Fasting hypoglycemia": "Find and correct the underlying cause and adjust the offending drug",
                    "Reactive hypoglycemia": "Frequent meals, less refined sugar, and more physical activity",
                    "Idiopathic postprandial syndrome": "Frequent snacks and avoidance of simple sugars in the diet"
                }
            }
        },
        {
            "slug": "causes_of_fasting_hypoglycemia",
            "title": "SHAKIER: Causes of Fasting Hypoglycemia",
            "subtitle": "Match each cause to its mechanism, the patient it shows up in, and its key test finding",
            "categories": ["Mechanism of the low glucose", "Typical patient clue", "Key test finding"],
            "data": {
                "Sulfonylureas and meglitinides": {
                    "Mechanism of the low glucose": "Drug drives pancreatic beta cells to secrete more insulin",
                    "Typical patient clue": "Type 2 diabetic who took an extra dose of glyburide for a high reading",
                    "Key test finding": "Positive sulfonylurea screen with elevated C-peptide"
                },
                "Alcohol use": {
                    "Mechanism of the low glucose": "Ethanol metabolism raises NADH, blocking lactate conversion to pyruvate",
                    "Typical patient clue": "Heavy drinker brought in confused and tremulous with an elevated alcohol level",
                    "Key test finding": "High NADH and low NAD+, with a low insulin level"
                },
                "Chronic kidney disease": {
                    "Mechanism of the low glucose": "Insulin is renally cleared, so poor filtration lets insulin accumulate",
                    "Typical patient clue": "Anorexic patient with failing kidneys taking insulin or oral agents",
                    "Key test finding": "Reduced renal filtration with a raised insulin level"
                },
                "Advanced liver disease": {
                    "Mechanism of the low glucose": "Diseased liver cannot perform gluconeogenesis or glycogenolysis",
                    "Typical patient clue": "Patient with alcoholic cirrhosis, the setting where this is most common",
                    "Key test finding": "Liver tests may be abnormal, but normal values do not exclude it"
                },
                "Insulinoma": {
                    "Mechanism of the low glucose": "Islet beta-cell tumor releases large amounts of insulin autonomously",
                    "Typical patient clue": "Nondiabetic adult with repeated fasting spells and no drug exposure",
                    "Key test finding": "Markedly raised insulin and proinsulin with a negative drug screen"
                },
                "Cortisol deficiency": {
                    "Mechanism of the low glucose": "Loss of a counterregulatory hormone that normally raises glucose",
                    "Typical patient clue": "Patient with suspected primary or central adrenal insufficiency",
                    "Key test finding": "Low morning cortisol confirmed with an ACTH stimulation test"
                }
            }
        },
        {
            "slug": "insulin_lab_patterns",
            "title": "Reading the Insulin Panel",
            "subtitle": "Place each laboratory value under the cause of hyperinsulinemic hypoglycemia it points to",
            "categories": ["Factitious insulin use", "Factitious sulfonylurea use", "Insulinoma"],
            "data": {
                "Insulin level": {
                    "Factitious insulin use": "Elevated from the injected drug itself",
                    "Factitious sulfonylurea use": "Normal to mildly elevated",
                    "Insulinoma": "Markedly elevated, the highest of the three"
                },
                "Proinsulin level": {
                    "Factitious insulin use": "Normal to low, since injected insulin contains no precursor",
                    "Factitious sulfonylurea use": "Normal to mildly elevated",
                    "Insulinoma": "Markedly elevated along with insulin"
                },
                "C-peptide level": {
                    "Factitious insulin use": "Normal to low, absent from pharmacologic insulin",
                    "Factitious sulfonylurea use": "Elevated because the drug stimulates the patient's own beta cells",
                    "Insulinoma": "Elevated from autonomous tumor secretion"
                },
                "Sulfonylurea screen": {
                    "Factitious insulin use": "Absent, no drug detected in serum",
                    "Factitious sulfonylurea use": "Present, which is what identifies covert drug use",
                    "Insulinoma": "Absent, no drug detected in serum"
                },
                "Underlying problem": {
                    "Factitious insulin use": "Self-administered injections of preprocessed pharmacologic insulin",
                    "Factitious sulfonylurea use": "Covert ingestion of an antihyperglycemic pill",
                    "Insulinoma": "Rare tumor of the pancreatic islet beta cells"
                }
            }
        },
        {
            "slug": "diagnosis_and_treatment_tools",
            "title": "Diagnosing and Treating Hypoglycemia",
            "subtitle": "Match each test or treatment to what it is, when it is used, and its key detail",
            "categories": ["What it is", "When it is used", "Key detail or threshold"],
            "data": {
                "Whipple triad": {
                    "What it is": "Low glucose plus typical symptoms, both corrected by giving glucose",
                    "When it is used": "Establishing the diagnosis of hypoglycemia, especially without diabetes",
                    "Key detail or threshold": "70 mg/dL or below is the general-population alert value"
                },
                "Supervised 72-hour fast": {
                    "What it is": "Inpatient fast with glucose and insulin drawn every 6 hours",
                    "When it is used": "Unexplained fasting hypoglycemia after initial testing is inconclusive",
                    "Key detail or threshold": "Ended for symptoms or a glucose below 55 mg/dL"
                },
                "Mixed meal test": {
                    "What it is": "Supervised meal after an overnight fast with hourly glucose for 5 hours",
                    "When it is used": "Confirming suspected reactive, postprandial hypoglycemia",
                    "Key detail or threshold": "Positive if symptoms occur below 55 mg/dL; poorly reproducible"
                },
                "Intravenous dextrose": {
                    "What it is": "Sugar given directly into the vein, with glucagon as an alternative",
                    "When it is used": "Symptomatic patient with altered mental status who cannot swallow safely",
                    "Key detail or threshold": "Given immediately to prevent irreversible neurologic damage"
                },
                "Acarbose or miglitol": {
                    "What it is": "Alpha-glucosidase inhibitors that block brush-border carbohydrate digestion",
                    "When it is used": "Reactive hypoglycemia that persists despite dietary change",
                    "Key detail or threshold": "Slow absorption blunts the postprandial glucose and insulin spike"
                },
                "Octreotide or diazoxide": {
                    "What it is": "Agents that suppress pancreatic insulin release",
                    "When it is used": "Selected hyperinsulinemic hypoglycemia under specialist management",
                    "Key detail or threshold": "Used for unresectable insulinoma or persistent post-bariatric spells"
                }
            }
        }
    ]
}
