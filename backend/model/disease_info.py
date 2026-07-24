
NOT_A_LEAF_LABEL = "Unrecognized — doesn't look like a clear leaf photo"

DISEASE_INFO: dict[str, dict[str, str]] = {
    "Apple___Apple_scab": {
        "causes": "Caused by the fungus Venturia inaequalis, which "
                  "overwinters in fallen leaves and spreads via spores "
                  "during wet spring weather.",
        "symptoms": "Olive-green to black velvety spots on leaves and "
                    "fruit, often with a scabby, rough texture. Leaves "
                    "may yellow and drop early.",
        "treatment": "Remove and destroy fallen leaves each autumn. "
                     "Apply a fungicide labeled for apple scab starting "
                     "at bud break and repeating on a 7-10 day schedule "
                     "during wet periods.",
        "prevention": "Choose scab-resistant apple varieties, prune for "
                      "good air circulation, and avoid overhead watering "
                      "that keeps foliage wet.",
    },
    "Apple___Black_rot": {
        "causes": "Caused by the fungus Botryosphaeria obtusa, which "
                  "survives in dead wood, mummified fruit, and cankers "
                  "on the tree.",
        "symptoms": "Purple-bordered brown leaf spots ('frogeye leaf "
                    "spot'), rotted fruit with concentric rings, and "
                    "sunken bark cankers on branches.",
        "treatment": "Prune out dead or cankered wood and remove "
                     "mummified fruit. Apply fungicide sprays timed with "
                     "apple scab treatments during the growing season.",
        "prevention": "Sanitize the orchard floor each season, avoid "
                      "wounding bark, and maintain tree vigor with proper "
                      "fertilization and watering.",
    },
    "Apple___Cedar_apple_rust": {
        "causes": "Caused by the fungus Gymnosporangium juniperi-"
                  "virginianae, which requires both apple and juniper/"
                  "cedar trees to complete its life cycle.",
        "symptoms": "Bright yellow-orange spots on upper leaf surfaces "
                    "that later develop tube-like structures on the "
                    "underside; can also affect fruit.",
        "treatment": "Apply protective fungicides in spring when orange "
                     "gelatinous galls appear on nearby junipers and "
                     "spores are released.",
        "prevention": "Remove nearby juniper or cedar hosts if "
                      "practical, or plant rust-resistant apple "
                      "varieties when junipers can't be removed.",
    },
    "Apple___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Continue routine care: regular watering, "
                      "balanced fertilization, and periodic inspection "
                      "for early signs of disease.",
    },
    "Blueberry___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Maintain acidic, well-drained soil, consistent "
                      "moisture, and good air circulation between "
                      "bushes.",
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "causes": "Caused by the fungus Podosphaera clandestina, "
                  "favored by warm days, cool nights, and shaded, "
                  "poorly ventilated canopies.",
        "symptoms": "White powdery patches on young leaves and shoots, "
                    "which may curl, distort, or stunt in growth.",
        "treatment": "Apply sulfur- or potassium bicarbonate-based "
                     "fungicides at the first sign of white patches, "
                     "repeating per label instructions.",
        "prevention": "Prune to improve airflow and sunlight "
                      "penetration, and avoid excess nitrogen "
                      "fertilizer that promotes susceptible new growth.",
    },
    "Cherry_(including_sour)___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Maintain good pruning practices for airflow and "
                      "monitor regularly for early mildew or spot "
                      "symptoms.",
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "causes": "Caused by the fungus Cercospora zeae-maydis, which "
                  "thrives in warm, humid conditions and survives in "
                  "corn residue left on the field.",
        "symptoms": "Small, rectangular tan-to-gray lesions running "
                    "parallel to leaf veins, which can merge and cause "
                    "significant leaf blighting.",
        "treatment": "Apply a labeled foliar fungicide if disease "
                     "pressure is high, especially before tasseling in "
                     "susceptible fields.",
        "prevention": "Rotate crops away from corn, till under crop "
                      "residue, and plant resistant hybrids in fields "
                      "with a history of this disease.",
    },
    "Corn_(maize)___Common_rust_": {
        "causes": "Caused by the fungus Puccinia sorghi, whose spores "
                  "are wind-dispersed and favor cool, moist weather.",
        "symptoms": "Small, reddish-brown, elongated pustules scattered "
                    "on both leaf surfaces, which can turn dark brown to "
                    "black as they age.",
        "treatment": "Apply a foliar fungicide if pustules are numerous "
                     "and appear early in the season on susceptible "
                     "hybrids.",
        "prevention": "Plant rust-resistant hybrids, which is the most "
                      "effective and common control for this disease.",
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "causes": "Caused by the fungus Exserohilum turcicum, favored "
                  "by moderate temperatures, high humidity, and "
                  "extended leaf wetness.",
        "symptoms": "Long, cigar-shaped gray-green to tan lesions on "
                    "leaves that can expand and cause extensive leaf "
                    "death.",
        "treatment": "Apply a labeled fungicide when lesions appear "
                     "before or during tasseling, particularly in "
                     "high-risk fields.",
        "prevention": "Rotate crops, till under infected residue, and "
                      "select hybrids with resistance to this disease.",
    },
    "Corn_(maize)___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Continue crop rotation and monitor fields "
                      "periodically for early disease symptoms.",
    },
    "Grape___Black_rot": {
        "causes": "Caused by the fungus Guignardia bidwellii, which "
                  "overwinters in mummified berries and infected canes.",
        "symptoms": "Small tan spots with dark borders on leaves, and "
                    "berries that shrivel into hard black 'mummies'.",
        "treatment": "Remove mummified berries and infected canes "
                     "during dormant pruning. Apply fungicide sprays "
                     "starting at bud break through fruit development.",
        "prevention": "Improve canopy airflow through pruning, and "
                      "clean up fallen leaves and fruit each season.",
    },
    "Grape___Esca_(Black_Measles)": {
        "causes": "Caused by a complex of fungi that infect through "
                  "pruning wounds and colonize the vine's woody tissue "
                  "over multiple years.",
        "symptoms": "'Tiger-stripe' interveinal streaking on leaves, "
                    "and dark spotted or measle-like discoloration on "
                    "berries; vines may decline suddenly.",
        "treatment": "No reliable curative fungicide exists; remove and "
                     "destroy severely affected wood or vines to slow "
                     "spread.",
        "prevention": "Prune during dry weather, protect large pruning "
                      "wounds with a sealant, and avoid stressing "
                      "established vines.",
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "causes": "Caused by the fungus Pseudocercospora vitis "
                  "(Isariopsis leaf spot), which spreads in warm, humid "
                  "conditions.",
        "symptoms": "Irregular dark brown to reddish-brown spots on "
                    "leaves that can merge and cause premature leaf "
                    "drop.",
        "treatment": "Apply labeled fungicides during the growing "
                     "season if spotting is significant, especially in "
                     "wet years.",
        "prevention": "Improve air circulation through canopy "
                      "management and remove fallen infected leaves.",
    },
    "Grape___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Maintain good canopy management and monitor for "
                      "early signs of fungal disease.",
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "causes": "Caused by the bacterium Candidatus Liberibacter, "
                  "spread primarily by the Asian citrus psyllid insect.",
        "symptoms": "Blotchy, asymmetric yellow mottling on leaves, "
                    "stunted growth, and small, lopsided, bitter fruit "
                    "that stays green at the bottom.",
        "treatment": "There is no cure; infected trees should be "
                     "removed to prevent further spread, and psyllid "
                     "populations should be controlled with insecticide "
                     "programs.",
        "prevention": "Control the Asian citrus psyllid vector, use "
                      "certified disease-free nursery stock, and "
                      "monitor trees regularly for early symptoms.",
    },
    "Peach___Bacterial_spot": {
        "causes": "Caused by the bacterium Xanthomonas arboricola pv. "
                  "pruni, spread by wind-driven rain and favored by warm, "
                  "wet weather.",
        "symptoms": "Small, angular, water-soaked spots on leaves that "
                    "turn purple-black and may fall out leaving a "
                    "'shot-hole' look; fruit can develop pitted lesions.",
        "treatment": "Apply copper-based bactericides during dormant "
                     "and early growing season; there's no cure once "
                     "infection is established.",
        "prevention": "Plant resistant peach varieties, avoid overhead "
                      "irrigation, and prune for good air circulation.",
    },
    "Peach___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Maintain good orchard sanitation and monitor "
                      "regularly for early bacterial spot symptoms.",
    },
    "Pepper,_bell___Bacterial_spot": {
        "causes": "Caused by Xanthomonas species bacteria, spread by "
                  "splashing water, contaminated seed, and handling wet "
                  "plants.",
        "symptoms": "Small, water-soaked, dark spots on leaves that may "
                    "have a yellow halo; spots can also appear on fruit "
                    "as raised, scab-like lesions.",
        "treatment": "Apply copper-based bactericides early, though "
                     "efficacy is limited once infection spreads; remove "
                     "severely affected plants.",
        "prevention": "Use certified disease-free seed and "
                      "transplants, avoid overhead watering, and rotate "
                      "crops away from peppers and tomatoes.",
    },
    "Pepper,_bell___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Use disease-free seed, rotate crops, and avoid "
                      "working with wet plants to reduce bacterial "
                      "spread.",
    },
    "Potato___Early_blight": {
        "causes": "Caused by the fungus Alternaria solani, favored by "
                  "warm temperatures and alternating wet and dry "
                  "conditions.",
        "symptoms": "Dark brown spots with concentric 'target' rings, "
                    "usually starting on older, lower leaves and "
                    "expanding upward.",
        "treatment": "Apply a labeled fungicide at first sign of "
                     "symptoms and repeat on a regular schedule through "
                     "the season.",
        "prevention": "Rotate crops, avoid overhead irrigation, and "
                      "remove infected plant debris after harvest.",
    },
    "Potato___Late_blight": {
        "causes": "Caused by the oomycete Phytophthora infestans, "
                  "which spreads rapidly in cool, wet weather (the "
                  "pathogen behind the Irish potato famine).",
        "symptoms": "Water-soaked, dark green to black lesions on "
                    "leaves that spread quickly, often with white "
                    "fungal growth on the underside in humid conditions.",
        "treatment": "Apply protective fungicides preventively in "
                     "at-risk weather, and destroy infected plants "
                     "promptly since it spreads fast.",
        "prevention": "Plant certified disease-free seed potatoes, "
                      "avoid overhead watering, and destroy volunteer "
                      "potato plants and cull piles.",
    },
    "Potato___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Rotate crops and monitor regularly, especially "
                      "during cool, wet weather when blight risk is "
                      "highest.",
    },
    "Raspberry___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Maintain good air circulation between canes and "
                      "monitor for early signs of fungal disease.",
    },
    "Soybean___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Rotate crops and monitor fields periodically for "
                      "early signs of fungal or bacterial disease.",
    },
    "Squash___Powdery_mildew": {
        "causes": "Caused by fungi such as Podosphaera xanthii and "
                  "Erysiphe cichoracearum, favored by warm days, high "
                  "humidity, and shaded conditions.",
        "symptoms": "White, powdery fungal growth on leaf surfaces and "
                    "stems, which can cause leaves to yellow and die "
                    "back if severe.",
        "treatment": "Apply sulfur, potassium bicarbonate, or other "
                     "labeled fungicides at first sign of white powdery "
                     "patches.",
        "prevention": "Space plants for good airflow, plant resistant "
                      "varieties, and avoid excess nitrogen fertilizer.",
    },
    "Strawberry___Leaf_scorch": {
        "causes": "Caused by the fungus Diplocarpon earlianum, favored "
                  "by wet foliage and warm temperatures.",
        "symptoms": "Small purple spots on leaves that enlarge and "
                    "merge, giving leaves a scorched, reddish-brown "
                    "appearance.",
        "treatment": "Apply a labeled fungicide during the growing "
                     "season if spotting is widespread, and remove "
                     "heavily infected leaves.",
        "prevention": "Remove old leaves after harvest, avoid overhead "
                      "watering, and space plants for good air "
                      "circulation.",
    },
    "Strawberry___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Remove old foliage after harvest and monitor for "
                      "early leaf scorch symptoms.",
    },
    "Tomato___Bacterial_spot": {
        "causes": "Caused by Xanthomonas species bacteria, spread by "
                  "splashing water, contaminated seed, and tools.",
        "symptoms": "Small, water-soaked, dark spots on leaves with "
                    "yellow halos, and scabby raised spots on fruit.",
        "treatment": "Apply copper-based bactericides early; severely "
                     "infected plants should be removed since there's "
                     "no cure once established.",
        "prevention": "Use certified disease-free seed and "
                      "transplants, rotate crops, and avoid overhead "
                      "watering.",
    },
    "Tomato___Early_blight": {
        "causes": "Caused by the fungus Alternaria solani, favored by "
                  "warm temperatures and alternating wet and dry "
                  "conditions.",
        "symptoms": "Dark brown spots with concentric 'target' rings, "
                    "typically starting on older, lower leaves.",
        "treatment": "Apply a labeled fungicide at first symptoms and "
                     "repeat on a regular schedule; remove heavily "
                     "infected leaves.",
        "prevention": "Rotate crops, stake plants for airflow, and "
                      "mulch to reduce soil splash onto leaves.",
    },
    "Tomato___Late_blight": {
        "causes": "Caused by the oomycete Phytophthora infestans, "
                  "which spreads rapidly in cool, wet weather.",
        "symptoms": "Water-soaked, dark green to black lesions on "
                    "leaves and stems that spread quickly, often with "
                    "white fungal growth on leaf undersides.",
        "treatment": "Apply protective fungicides preventively in "
                     "at-risk weather, and remove and destroy infected "
                     "plants promptly.",
        "prevention": "Avoid overhead watering, space plants for "
                      "airflow, and avoid planting near infected "
                      "potatoes.",
    },
    "Tomato___Leaf_Mold": {
        "causes": "Caused by the fungus Passalora fulva (formerly "
                  "Cladosporium fulvum), favored by high humidity, "
                  "especially in greenhouses.",
        "symptoms": "Pale yellow spots on upper leaf surfaces with "
                    "olive-green to grayish-purple fuzzy mold growth on "
                    "the underside.",
        "treatment": "Improve ventilation and reduce humidity; apply a "
                     "labeled fungicide if the problem persists.",
        "prevention": "Space plants well, ventilate greenhouses "
                      "thoroughly, and avoid wetting foliage when "
                      "watering.",
    },
    "Tomato___Septoria_leaf_spot": {
        "causes": "Caused by the fungus Septoria lycopersici, which "
                  "spreads via splashing water and survives in plant "
                  "debris.",
        "symptoms": "Small, circular spots with dark borders and gray "
                    "centers, often with tiny black specks (fungal "
                    "fruiting bodies) visible in the center.",
        "treatment": "Remove infected lower leaves promptly and apply "
                     "a labeled fungicide during wet periods.",
        "prevention": "Mulch around plants, avoid overhead watering, "
                      "and rotate crops away from tomatoes each season.",
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "causes": "Caused by an infestation of two-spotted spider "
                  "mites (Tetranychus urticae), tiny pests that thrive "
                  "in hot, dry conditions.",
        "symptoms": "Fine yellow stippling or speckling on leaves, "
                    "sometimes with visible fine webbing; leaves may "
                    "bronze and dry out under heavy infestation.",
        "treatment": "Apply insecticidal soap or a labeled miticide, "
                     "and rinse plants with water to knock down mite "
                     "populations.",
        "prevention": "Keep plants well-watered to reduce heat stress, "
                      "and encourage natural predators like predatory "
                      "mites and ladybugs.",
    },
    "Tomato___Target_Spot": {
        "causes": "Caused by the fungus Corynespora cassiicola, "
                  "favored by warm, humid conditions and prolonged leaf "
                  "wetness.",
        "symptoms": "Brown lesions with concentric target-like rings, "
                    "similar to early blight, which can appear on "
                    "leaves, stems, and fruit.",
        "treatment": "Apply a labeled fungicide and remove heavily "
                     "infected foliage to slow spread.",
        "prevention": "Improve air circulation, avoid overhead "
                      "watering, and rotate crops away from "
                      "susceptible hosts.",
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "causes": "Caused by a virus transmitted by the silverleaf "
                  "whitefly (Bemisia tabaci); once a plant is infected "
                  "there is no cure.",
        "symptoms": "Upward curling and yellowing of leaves, stunted "
                    "growth, and significantly reduced fruit "
                    "production.",
        "treatment": "Remove and destroy infected plants to reduce "
                     "virus reservoirs, and control whitefly populations "
                     "with insecticides or sticky traps.",
        "prevention": "Use whitefly-resistant or virus-resistant "
                      "varieties, use reflective mulches, and control "
                      "whiteflies early in the season.",
    },
    "Tomato___Tomato_mosaic_virus": {
        "causes": "Caused by Tomato mosaic virus, which spreads "
                  "through contaminated tools, hands, and infected "
                  "seed; it is highly stable and persistent.",
        "symptoms": "Mottled light and dark green mosaic patterning on "
                    "leaves, leaf curling, and stunted or distorted "
                    "growth.",
        "treatment": "There's no cure; remove and destroy infected "
                     "plants and disinfect tools and hands thoroughly "
                     "after handling them.",
        "prevention": "Use certified virus-free seed, wash hands and "
                      "tools between plants, and avoid tobacco product "
                      "use around plants (a known virus source).",
    },
    "Tomato___healthy": {
        "causes": "No disease detected — the leaf appears healthy.",
        "symptoms": "Uniform green color with no spots, lesions, or "
                    "discoloration.",
        "treatment": "No treatment needed.",
        "prevention": "Rotate crops, avoid overhead watering, and "
                      "monitor regularly for early signs of disease or "
                      "pests.",
    },
    NOT_A_LEAF_LABEL: {
        "causes": "The model's top confidence for this image was below the "
                  "reliability threshold, meaning it doesn't closely "
                  "resemble any of the trained disease classes.",
        "symptoms": "N/A — no diagnosis was reliable enough to report.",
        "treatment": "Try a clearer photo: fill most of the frame with a "
                     "single leaf, use natural daylight, and avoid heavy "
                     "shadows or blur.",
        "prevention": "N/A",
    },
}


DEFAULT_INFO = {
    "causes": "Detailed information for this class hasn't been added yet.",
    "symptoms": "Detailed information for this class hasn't been added yet.",
    "treatment": "Detailed information for this class hasn't been added yet.",
    "prevention": "Detailed information for this class hasn't been added yet.",
}


def get_disease_info(disease_name: str) -> dict[str, str]:
    return DISEASE_INFO.get(disease_name, DEFAULT_INFO)