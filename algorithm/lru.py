def lru_algorithm(reference_string, num_frames):
    frames = []
    page_faults = 0
    recent_usage = {}
    result = []

    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                lru_page = min(frames, key=lambda x: recent_usage[x])
                frames[frames.index(lru_page)] = page
            page_faults += 1
            fault = "Yes"
        else:
            fault = "No"
        
        recent_usage[page] = i
        result.append((i + 1, page, list(frames), fault))

    return result, page_faults
