import torch
import torch.nn.functional as F
from tqdm import tqdm
import csv

from utils.dice_score import (
    dice_coefficient,
    dice_coefficient_loss,
    dice_coefficient_score,
    multi_class_score,
)
import torchio as tio

# anchor = [
#     "Background",  # 0
#     "BrainStem.nrrd",  # 1
#     "Mandible.nrrd",  # 3
# ]

anchor = [
    "background",
    "Brain Stem.nrrd",  # 2
    "Eye-L.nrrd",  # 6
    "Eye-R.nrrd",  # 7
    "Mandible.nrrd",  # 12
    "Spinal Cord.nrrd",  # 21
    "TMJL.nrrd",  # 26
    "TMJR.nrrd",  # 27
    "Trachea.nrrd",  # 28
]


def evaluate(net, dataloader, device):
    net.eval()
    num_val_batches = len(dataloader)
    dice_score = 0

    # print(num_val_batches)
    # iterate over the validation set
    dice_scores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    class_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for batch in tqdm(
        dataloader,
        total=num_val_batches,
        desc="Validation round",
        unit="batch",
        leave=False,
    ):
        images = batch["image"][tio.DATA]
        true_masks = batch["mask"][tio.DATA]

        # true_masks = true_masks.squeeze(0)
        # image = torch.unsqueeze(image, 0)
        # move images and labels to correct device and type
        images = images.to(device=device, dtype=torch.float32)
        true_masks = true_masks.to(device=device, dtype=torch.long)
        # true_masks = true_masks.float()

        with torch.no_grad():

            mask_pred = net(images)

            true_masks = torch.squeeze(true_masks, 0)

            # repeat for loss
            all_dice_score, list_scores, classes = multi_class_score(
                mask_pred, true_masks.float()
            )

            dice_score += all_dice_score

            for i, class_score in enumerate(list_scores):
                dice_scores[i] += class_score

            for i in classes:
                class_counter[i] += 1

    for i, class_instances in enumerate(class_counter):

        dice_scores[i] = dice_scores[i] / class_instances

    total = 0
    for i, score in enumerate(dice_scores):
        print(anchor[i] + " has dice " + str(score))
        if i > 0:
            total += score

    with open("new_data_anchor.csv", "a+", newline="") as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(dice_scores)

    total = total / 8
    net.train()
    return total
