import openai
import json

openai.api_key = "TA_CLE_API_OPENAI"

def analyser_avis(avis):
    prompt = f"""
Tu es un modérateur automatique pour une plateforme d’avis en ligne spécialisée dans les avis sur les professionnels de santé (médecins, dentistes, kinés, etc.).

Ta mission est d’analyser un avis rédigé par un patient et de déterminer s’il est conforme aux règles suivantes :
- Aucun détail médical personnel ou de santé ne doit apparaître (diagnostic, pathologie, traitement spécifique).
- Aucun propos diffamatoire, insultant ou discriminatoire ne doit être accepté.
- L’avis doit être factuel et porter uniquement sur des critères d’expérience patient (ponctualité, accueil, clarté des explications, accessibilité, etc.).
- Les avis extrêmement vagues ou sans valeur informative doivent être rejetés (exemple : "Médecin nul" sans justification).

Retourne ta réponse sous la forme d’un objet JSON avec les clés suivantes :
- `accept` : `true` ou `false` selon que l’avis peut être publié immédiatement ou non.
- `reason` : Si l’avis est refusé, explique pourquoi (mention de santé personnelle, insulte, diffamation, avis trop vague, etc.).
- `sentiment` : Analyse la tonalité de l’avis, soit `"positif"`, `"neutre"`, ou `"négatif"`.
- `categories` : Liste des thèmes abordés dans l’avis, choisis parmi cette liste : `ponctualité`, `accueil`, `clarté des explications`, `facilité d’accès`, `tarification`, `qualité d’écoute`, `ressenti général`, `autre`.

Avis à analyser :
"""
{avis}
"""
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Tu es un assistant qui répond uniquement en JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500
    )

    content = response['choices'][0]['message']['content']
    return json.loads(content)

# Exemple d’utilisation
avis_test = "Le Dr Martin est sympa, mais il m’a prescrit un traitement pour mon asthme sans trop m’expliquer les effets secondaires."
resultat = analyser_avis(avis_test)

print(json.dumps(resultat, indent=4, ensure_ascii=False))
