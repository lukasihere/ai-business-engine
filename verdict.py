def verdict(data, score):
    if score < -50:
        return "Ide e dobët. Problemi nuk është tregu, je ti."
    if score < 0:
        return "Ide mesatare. Vetëm disiplinë ekstreme mund ta shpëtojë."
    return "Ka potencial. Tani puno, mos u ankoni."
