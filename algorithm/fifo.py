def fifo_algorithm(reference_string, num_frames):
    frames = []
    page_faults = 0
    result = []

    for step, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
            fault = "Yes"
        else:
            fault = "No"

        result.append((step + 1, page, list(frames), fault))

    return result, page_faults
