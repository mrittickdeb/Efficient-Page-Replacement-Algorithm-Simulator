def optimal_algorithm(reference_string, num_frames):
    frames = []
    page_faults = 0
    result = []

    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                future_use = {p: (reference_string[i:].index(p) if p in reference_string[i:] else float("inf")) for p in frames}
                farthest_page = max(future_use, key=future_use.get)
                frames[frames.index(farthest_page)] = page
            page_faults += 1
            fault = "Yes"
        else:
            fault = "No"
        
        result.append((i + 1, page, list(frames), fault))

    return result, page_faults
