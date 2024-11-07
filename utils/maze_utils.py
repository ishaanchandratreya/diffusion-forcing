def maze_name_to_maze_spec(env_id, eval_maze_name="default"):

    assert "custom" in env_id, "Only custom mazes supported"
    if eval_maze_name == "default":
        # conditioned on custom-v1 # add the defaults based on version default name
        return (
            "###############\\"
            + "#OOOOOOOOOOOOO#\\"
            + "#OOOOOOOOOO#OO#\\"
            + "#O####OOOOO#GO#\\"
            + "#O#OO#OOOOO#OO#\\"
            + "#O#OO#OOOOO#OO#\\"
            + "#OOOOOO###OOOO#\\"
            + "#OOOOOO###OOOO#\\"
            + "#OOOOOO###OOOO#\\"
            + "#O##########OO#\\"
            + "#OOOOOOOOOOOOO#\\"
            + "###############"
        )
    elif eval_maze_name == "unblocked":
        return (
            "###############\\"
            + "#OOOOOOOOOOOOO#\\"
            + "#OOOOOOOOOO#OO#\\"
            + "#O####OOOOO#GO#\\"
            + "#O#OO#OOOOO#OO#\\"
            + "#O#OO#OOOOO#OO#\\"
            + "#OOOOOOOOOOOOO#\\"
            + "#OOOOOOOOOOOOO#\\"
            + "#OOOOOOOOOOOOO#\\"
            + "#O##########OO#\\"
            + "#OOOOOOOOOOOOO#\\"
            + "###############"
        )
    else:
        raise NotImplementedError
