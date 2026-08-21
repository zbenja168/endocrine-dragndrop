BRICK = {
    "brick_num": 24,
    "brick_title": "Type 1 Diabetes Mellitus (T1DM)",
    "games": [
        {
            "slug": "insulin_loss_chain",
            "title": "What Breaks When Insulin Disappears",
            "subtitle": "Match each normal job of insulin to what fails without it and the clinical endpoint that follows",
            "categories": ["Insulin's normal job", "What fails without insulin", "Clinical endpoint"],
            "data": {
                "Glucose uptake into muscle and fat": {
                    "Insulin's normal job": "Drives GLUT4 translocation in skeletal muscle and adipose tissue",
                    "What fails without insulin": "Insulin-stimulated uptake falls sharply while glucose piles up in blood",
                    "Clinical endpoint": "Hyperglycemia with osmotic diuresis and fatigue"
                },
                "Fuel storage": {
                    "Insulin's normal job": "Stores glycogen, triglyceride, and protein as the master anabolic signal",
                    "What fails without insulin": "Storage stops and catabolism of fat and protein is unleashed",
                    "Clinical endpoint": "Weight loss occurring alongside polyphagia"
                },
                "Restraint of hepatic glucose output": {
                    "Insulin's normal job": "Holds the liver in storage mode between meals",
                    "What fails without insulin": "Gluconeogenesis and glycogenolysis proceed unchecked",
                    "Clinical endpoint": "Worsening fasting hyperglycemia"
                },
                "Suppression of lipolysis and ketogenesis": {
                    "Insulin's normal job": "Keeps free fatty acids out of the ketogenic pathway",
                    "What fails without insulin": "Free fatty acids are converted into ketone bodies",
                    "Clinical endpoint": "Risk of diabetic ketoacidosis"
                },
                "Suppression of glucagon": {
                    "Insulin's normal job": "Rises in the fed state and keeps the insulin-to-glucagon ratio high",
                    "What fails without insulin": "Glucagon becomes completely unopposed and the liver acts as if fasting",
                    "Clinical endpoint": "Amplified hyperglycemia and accelerated ketone production"
                }
            }
        },
        {
            "slug": "t1dm_vs_t2dm_labs",
            "title": "Type 1 versus Type 2 at the Bedside and in the Lab",
            "subtitle": "Sort each feature into the type of diabetes it characterizes",
            "categories": ["C-peptide", "Islet autoantibodies", "Nature of the insulin defect", "Risk of ketoacidosis", "Typical body habitus", "Tempo of symptom onset"],
            "data": {
                "Type 1 diabetes mellitus": {
                    "C-peptide": "Low or absent, reflecting destroyed beta cells",
                    "Islet autoantibodies": "Anti-GAD, IA-2, or ZnT8 usually present at diagnosis",
                    "Nature of the insulin defect": "Absolute deficiency after autoimmune beta-cell destruction",
                    "Risk of ketoacidosis": "High, and DKA may be the very first presentation",
                    "Typical body habitus": "Lean, often with recent unintentional weight loss",
                    "Tempo of symptom onset": "Abrupt, with symptoms progressing over days to weeks"
                },
                "Type 2 diabetes mellitus": {
                    "C-peptide": "Normal or elevated, reflecting preserved secretion",
                    "Islet autoantibodies": "Absent in the typical case",
                    "Nature of the insulin defect": "Relative deficiency in the setting of insulin resistance",
                    "Risk of ketoacidosis": "Low unless a major physiologic stress intervenes",
                    "Typical body habitus": "Overweight or obese",
                    "Tempo of symptom onset": "Gradual, with few catabolic features"
                }
            }
        },
        {
            "slug": "dm_diagnostic_tests",
            "title": "Diagnostic Thresholds for Diabetes Mellitus",
            "subtitle": "Match each test to its cutoff, the condition attached to it, and what it actually measures",
            "categories": ["Cutoff value", "Condition or caveat", "What it measures"],
            "data": {
                "Hemoglobin A1c": {
                    "Cutoff value": "6.5% or higher (48 mmol/mol or higher)",
                    "Condition or caveat": "A standardized assay is required, and a value below 6.5% does not exclude T1DM",
                    "What it measures": "Glycated fraction of hemoglobin, reflecting roughly 2 to 3 months of control"
                },
                "Fasting plasma glucose": {
                    "Cutoff value": "126 mg/dL or higher (7.0 mmol/L)",
                    "Condition or caveat": "No caloric intake for at least 8 hours before the draw",
                    "What it measures": "Plasma glucose in the fasted state"
                },
                "Random venous plasma glucose": {
                    "Cutoff value": "200 mg/dL or higher (11.1 mmol/L)",
                    "Condition or caveat": "Diagnostic only in a patient with symptoms of hyperglycemia or a hyperglycemic crisis",
                    "What it measures": "Plasma glucose at any time of day regardless of meals"
                },
                "Oral glucose tolerance test": {
                    "Cutoff value": "200 mg/dL or higher (11.1 mmol/L) at 2 hours",
                    "Condition or caveat": "Performed with a load equivalent to 75 g of glucose",
                    "What it measures": "Plasma glucose 2 hours after a standardized glucose challenge"
                },
                "Serum C-peptide": {
                    "Cutoff value": "No diagnostic cutoff for diabetes; interpreted against a concurrent glucose",
                    "Condition or caveat": "Cleaved from proinsulin, so it is absent from injected insulin preparations",
                    "What it measures": "Endogenous beta-cell function rather than the presence of diabetes"
                }
            }
        },
        {
            "slug": "t1dm_management",
            "title": "Managing Type 1 Diabetes",
            "subtitle": "Match each element of care to its purpose, a concrete example, and the caution attached to it",
            "categories": ["Purpose", "Concrete example", "Caution"],
            "data": {
                "Basal insulin": {
                    "Purpose": "Suppresses hepatic glucose output between meals and overnight",
                    "Concrete example": "Glargine or detemir given as the long-acting component",
                    "Caution": "Too little basal coverage allows fasting hyperglycemia and ketogenesis"
                },
                "Bolus insulin": {
                    "Purpose": "Covers the postprandial glucose rise from each meal",
                    "Concrete example": "Lispro or aspart taken with meals",
                    "Caution": "Doses must be matched to carbohydrate intake to avoid post-meal hypoglycemia"
                },
                "Insulin pump therapy": {
                    "Purpose": "Delivers insulin continuously for tighter and more flexible control",
                    "Concrete example": "Continuous subcutaneous infusion, or a hybrid closed-loop paired with a monitor",
                    "Caution": "Favored for variable schedules or recurrent hypoglycemia, but interruption invites DKA"
                },
                "Continuous glucose monitoring": {
                    "Purpose": "Gives the patient a live feedback loop on the glucose response to insulin",
                    "Concrete example": "Recommended for anyone taking insulin or drugs that cause hypoglycemia",
                    "Caution": "Meter checks remain a backup, timed to the regimen rather than a fixed schedule"
                },
                "HbA1c monitoring": {
                    "Purpose": "Tracks longer-term glycemic control against a target",
                    "Concrete example": "Twice yearly when stable and at goal, roughly every 3 months when goals are unmet",
                    "Caution": "Target below 7% for most, relaxed toward 8% in older adults at risk from hypoglycemia"
                },
                "Patient education": {
                    "Purpose": "Prevents avoidable acute events by teaching self-recognition and self-adjustment",
                    "Concrete example": "Sick-day rules, exercise guidance, and recognizing shakiness, confusion, and diaphoresis",
                    "Caution": "Untreated hypoglycemia or missed doses during illness are common preventable triggers"
                }
            }
        }
    ]
}
