def count_skills(tree, required):
    learned = set()
    final_skill = tree[0]
    for skill in required:
        learned.add(skill)
        while skill != final_skill:
            skill = tree[skill]
            learned.add(skill)
    return len(learned)
