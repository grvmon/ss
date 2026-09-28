def sync_hero(source_file, target_file):
    with open(source_file, "r", encoding="utf-8") as f:
        src = f.read()
    with open(target_file, "r", encoding="utf-8") as f:
        tgt = f.read()

    start_marker = '<h1 class="hero-main-title">'
    end_marker = '<!-- CTA buttons group -->'

    src_start = src.find(start_marker)
    src_end = src.find(end_marker, src_start)
    
    tgt_start = tgt.find(start_marker)
    tgt_end = tgt.find(end_marker, tgt_start)

    if src_start != -1 and src_end != -1 and tgt_start != -1 and tgt_end != -1:
        hero_block = src[src_start:src_end]
        new_tgt = tgt[:tgt_start] + hero_block + tgt[tgt_end:]
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(new_tgt)
        print(f"Synced hero to {target_file}")
    else:
        print(f"Failed to find markers for {target_file}")

sync_hero("household-goods-storage/index.html", "household-goods-storage.html")
sync_hero("business-storage/index.html", "business-storage.html")
