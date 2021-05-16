model_path = "./densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 96% test auc 67% last to 14_14 layer unfreeze_new augmentation_zoom.h5"
model = models.load_model(model_path, backbone_name='densenet121', convert=True, nms=False)
