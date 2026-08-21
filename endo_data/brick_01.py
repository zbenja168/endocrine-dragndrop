BRICK = {
    "brick_num": 1,
    "brick_title": "Functional Endocrine Pathways",
    "games": [
        {
            "slug": "control_elements",
            "title": "Control Elements of an Endocrine Pathway",
            "subtitle": "Match each control element to its definition, its place in the reflex arc, and its HPT-axis example",
            "categories": ["Definition", "Place in the reflex arc", "HPT axis example"],
            "data": {
                "Stimulus": {
                    "Definition": "The physiological change that initiates the pathway",
                    "Place in the reflex arc": "The initiating event, upstream of every other element",
                    "HPT axis example": "Circulating T3/T4 falls below the set point"
                },
                "Sensor": {
                    "Definition": "The structure that detects the change and sends afferent signal",
                    "Place in the reflex arc": "First structure in the loop; feeds the integrating center",
                    "HPT axis example": "Hypothalamic neurons detecting low T3/T4"
                },
                "Integrating center": {
                    "Definition": "Compares afferent input against the set point and coordinates the response",
                    "Place in the reflex arc": "Decision point that launches the efferent limb",
                    "HPT axis example": "Hypothalamus secreting TRH into the portal system"
                },
                "Feedback signal": {
                    "Definition": "Pathway output that loops back to suppress or amplify the stimulus",
                    "Place in the reflex arc": "Closing step that returns output to earlier levels",
                    "HPT axis example": "Rising T3/T4 suppressing TRH and TSH secretion"
                }
            }
        },
        {
            "slug": "molecular_components",
            "title": "Molecular Signaling Components",
            "subtitle": "Match each signaling component to its job, its location, and how it appears in the HPT axis",
            "categories": ["What it does", "Where it is found", "HPT axis example"],
            "data": {
                "Hormone": {
                    "What it does": "Chemical messenger released to act on distant target cells",
                    "Where it is found": "Traveling in portal or systemic circulation between cells",
                    "HPT axis example": "TRH, TSH, and thyroxine (T4)"
                },
                "Receptor": {
                    "What it does": "Binds hormone with high specificity to initiate signaling",
                    "Where it is found": "Cell surface for peptides; intracellular for steroid and thyroid hormones",
                    "HPT axis example": "G-protein-coupled TRH receptor on pituitary thyrotrophs"
                },
                "Intracellular intermediates": {
                    "What it does": "Second messengers and kinases that amplify and relay the signal",
                    "Where it is found": "Inside the target cell, between receptor and response",
                    "HPT axis example": "Second-messenger cascade driving TSH release from the thyrotroph"
                },
                "Effector output": {
                    "What it does": "The measurable physiological change the cascade produces",
                    "Where it is found": "At the target tissue, the end of the signaling chain",
                    "HPT axis example": "T3-driven gene expression altering metabolism and thermogenesis"
                }
            }
        },
        {
            "slug": "hormone_classes",
            "title": "Hormone Classes at a Glance",
            "subtitle": "Match each hormone class to its synthesis, solubility, receptor location, and an example",
            "categories": ["Synthesis", "Solubility", "Receptor location", "Example"],
            "data": {
                "Peptides and proteins": {
                    "Synthesis": "Made as prohormones requiring further processing to activate",
                    "Solubility": "Hydrophilic",
                    "Receptor location": "Cell membrane receptors coupled to second messengers",
                    "Example": "Insulin, prolactin, follicle-stimulating hormone"
                },
                "Catecholamines and other hydrophilic amines": {
                    "Synthesis": "Made from the amino acids tyrosine, tryptophan, and histidine",
                    "Solubility": "Hydrophilic",
                    "Receptor location": "Cell membrane receptors",
                    "Example": "Dopamine, epinephrine, serotonin, histamine"
                },
                "Thyroid hormones": {
                    "Synthesis": "Iodinated amine derivatives built on tyrosine",
                    "Solubility": "Lipophilic",
                    "Receptor location": "Nuclear receptors inside the target cell",
                    "Example": "Thyroxine (T4) and triiodothyronine (T3)"
                },
                "Steroids": {
                    "Synthesis": "Synthesized from cholesterol",
                    "Solubility": "Lipophilic",
                    "Receptor location": "Intracellular ligand-activated transcription factors",
                    "Example": "Cortisol, estrogen, testosterone"
                }
            }
        },
        {
            "slug": "hpt_node_disruption",
            "title": "Localizing the Lesion in the HPT Axis",
            "subtitle": "Sort each feature under the disruption pattern it belongs to",
            "categories": ["Disrupted node", "TSH level", "T3/T4 level", "Mechanism"],
            "data": {
                "Primary hypothyroidism": {
                    "Disrupted node": "Thyroid gland",
                    "TSH level": "High",
                    "T3/T4 level": "Low, with an intact pituitary drive",
                    "Mechanism": "T3/T4 absent, so negative feedback on TSH is lost"
                },
                "Secondary hypothyroidism": {
                    "Disrupted node": "Anterior pituitary",
                    "TSH level": "Low",
                    "T3/T4 level": "Low, because the gland is never stimulated",
                    "Mechanism": "TSH signal absent, so the thyroid is unstimulated"
                },
                "TSH-secreting pituitary adenoma": {
                    "Disrupted node": "Pituitary adenoma",
                    "TSH level": "High despite elevated thyroid hormone",
                    "T3/T4 level": "High",
                    "Mechanism": "TSH produced autonomously, so feedback is bypassed"
                }
            }
        }
    ]
}
