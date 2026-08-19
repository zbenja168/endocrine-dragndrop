BRICK = {
    "brick_num": 23,
    "brick_title": "Structure and Function of the Endocrine Pancreas",
    "games": [
        {
            "slug": "islet_hormones",
            "title": "Hormones of the Endocrine Pancreas",
            "subtitle": "Match each peptide to the cell that makes it, what prompts its release, and its main role",
            "categories": ["Cell or tissue of origin", "What prompts its release", "Main role"],
            "data": {
                "Insulin": {
                    "Cell or tissue of origin": "Beta cells, the most numerous endocrine cells of the islets",
                    "What prompts its release": "Hyperglycemia after a meal, reinforced by parasympathetic signals",
                    "Main role": "Storage hormone: drives glycogen, lipid, and protein formation"
                },
                "Glucagon": {
                    "Cell or tissue of origin": "Alpha cells, intermingled with beta cells in human islets",
                    "What prompts its release": "Hypoglycemia during fasting or exercise, plus sympathetic fight-or-flight signals",
                    "Main role": "Raises serum glucose by hepatic glycogenolysis and gluconeogenesis"
                },
                "Somatostatin (GHIH)": {
                    "Cell or tissue of origin": "Delta cells scattered throughout the islets of Langerhans",
                    "What prompts its release": "Local islet signals; separate pools exist in hypothalamus and gut",
                    "Main role": "Paracrine brake on both alpha-cell and beta-cell secretion"
                },
                "GLP-1": {
                    "Cell or tissue of origin": "Intestinal cells that cleave proglucagon instead of making glucagon",
                    "What prompts its release": "Food entering the gut, before absorbed glucose has fully arrived",
                    "Main role": "Incretin that activates beta cells and lowers serum glucose"
                },
                "C-peptide": {
                    "Cell or tissue of origin": "Beta-cell granules, cleaved off proinsulin during processing",
                    "What prompts its release": "Any stimulus for insulin release, secreted in equimolar amounts",
                    "Main role": "Marker of endogenous insulin; low when insulin is injected"
                }
            }
        },
        {
            "slug": "glut_transporters",
            "title": "The GLUT Transporter Family",
            "subtitle": "Sort each glucose transporter by where it sits, whether insulin controls it, and what it does",
            "categories": ["Main location", "Insulin dependence", "Functional job"],
            "data": {
                "GLUT1": {
                    "Main location": "Most cells, especially red blood cells and brain",
                    "Insulin dependence": "Insulin-independent, providing constant basal uptake",
                    "Functional job": "Keeps obligate glucose users supplied regardless of insulin level"
                },
                "GLUT2": {
                    "Main location": "Pancreatic beta islet cells and hepatocytes",
                    "Insulin dependence": "Insulin-independent, so it senses glucose rather than responding to insulin",
                    "Functional job": "First step of beta-cell glucose sensing and hepatic glucose entry"
                },
                "GLUT3": {
                    "Main location": "Brain and placenta",
                    "Insulin dependence": "Insulin-independent uptake for high-priority tissues",
                    "Functional job": "Supplies neurons and fetal tissue with glucose continuously"
                },
                "GLUT4": {
                    "Main location": "Skeletal and cardiac muscle and adipose tissue",
                    "Insulin dependence": "Insulin-dependent translocation, though muscle contraction moves it too",
                    "Functional job": "Carries out the actual insulin-stimulated fall in serum glucose"
                },
                "GLUT5": {
                    "Main location": "Small intestine, muscle, and testes",
                    "Insulin dependence": "Not regulated by insulin at all",
                    "Functional job": "Transports fructose rather than glucose"
                }
            }
        },
        {
            "slug": "insulin_vs_glucagon",
            "title": "Insulin versus Glucagon",
            "subtitle": "Sort each feature into the hormone it belongs to",
            "categories": ["Insulin", "Glucagon"],
            "data": {
                "Islet cell of origin": {
                    "Insulin": "Beta cells, the largest proportion of islet endocrine cells",
                    "Glucagon": "Alpha cells, intermingled among the beta cells"
                },
                "Precursor molecule": {
                    "Insulin": "Preproinsulin cleaved to proinsulin, then to insulin plus C-peptide",
                    "Glucagon": "Proglucagon, which the gut can instead process into GLP-1"
                },
                "Receptor type": {
                    "Insulin": "Receptor tyrosine kinase that also binds IGF-1",
                    "Glucagon": "G protein-coupled receptor, densest on hepatocytes"
                },
                "Signaling events": {
                    "Insulin": "Tyrosine autophosphorylation, then PI3K and MAP kinase arms",
                    "Glucagon": "Adenylate cyclase raises cAMP, which activates protein kinase A"
                },
                "Effect on liver glycogen": {
                    "Insulin": "Promotes glycogen synthesis and storage after a meal",
                    "Glucagon": "Activates phosphorylase a to break glycogen down within minutes"
                },
                "Autonomic stimulus for release": {
                    "Insulin": "Parasympathetic rest-and-digest signaling after eating",
                    "Glucagon": "Sympathetic fight-or-flight signaling during stress or exercise"
                }
            }
        },
        {
            "slug": "beta_cell_secretion",
            "title": "How the Beta Cell Senses Glucose",
            "subtitle": "Match each player in the secretion cascade to its role, its trigger, and what happens next",
            "categories": ["Role in the beta cell", "What activates or changes it", "Immediate downstream result"],
            "data": {
                "GLUT2 transporter": {
                    "Role in the beta cell": "Insulin-independent doorway for glucose into the cell",
                    "What activates or changes it": "A sustained rise in serum glucose after a meal",
                    "Immediate downstream result": "Intracellular glucose becomes available for glycolysis"
                },
                "Glycolysis": {
                    "Role in the beta cell": "Metabolic step that converts glucose entry into an energy signal",
                    "What activates or changes it": "Arrival of glucose inside the beta cell",
                    "Immediate downstream result": "ATP generation raises the ATP-to-ADP ratio"
                },
                "ATP-sensitive potassium channel": {
                    "Role in the beta cell": "Sets the resting membrane potential of the beta cell",
                    "What activates or changes it": "A high ATP-to-ADP ratio, which closes the channel",
                    "Immediate downstream result": "Membrane depolarizes, becoming less negative"
                },
                "Voltage-gated calcium channel": {
                    "Role in the beta cell": "Links membrane voltage to intracellular signaling",
                    "What activates or changes it": "Depolarization of the beta-cell membrane",
                    "Immediate downstream result": "Calcium influx raises intracellular calcium"
                },
                "Insulin secretory granules": {
                    "Role in the beta cell": "Storage vesicles holding mature insulin and C-peptide",
                    "What activates or changes it": "Elevated intracellular calcium concentration",
                    "Immediate downstream result": "Exocytosis releases insulin into the bloodstream"
                }
            }
        }
    ]
}
