from pathlib import Path

from languages.tamil.lexora_txt_refinery.txt_cleaner import (
    refine_txt_file
)

from languages.tamil.lexora_json_refinery.json_cleaner import (
    refine_json_file
)

from languages.tamil.lexora_ocr.ocr_pipeline import (
    run_ocr_pipeline
)


def route_file(
    file_path: str
):

    suffix = Path(
        file_path
    ).suffix.lower()


    if suffix == ".txt":

        return refine_txt_file(
            file_path
        )


    if suffix == ".json":

        return refine_json_file(
            file_path
        )


    if suffix in [

        ".png",
        ".jpg",
        ".jpeg",
        ".webp"

    ]:

        return run_ocr_pipeline(
            file_path
        )


    raise ValueError(

        f"Unsupported file: {suffix}"

    )
