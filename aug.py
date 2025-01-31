from typing import Any, List

import albumentations as albu



# def get_transforms(size: int, scope: str = 'geometric', crop='random'):
#     augs = {'strong': albu.Compose([albu.HorizontalFlip(),
#                                     albu.ShiftScaleRotate(shift_limit=0.0, scale_limit=0.2, rotate_limit=20, p=.4),
#                                     albu.ElasticTransform(),
#                                     albu.OpticalDistortion(),
#                                     albu.OneOf([
#                                         albu.CLAHE(clip_limit=2),
#                                         albu.IAASharpen(),
#                                         albu.IAAEmboss(),
#                                         albu.RandomBrightnessContrast(),
#                                         albu.RandomGamma()
#                                     ], p=0.5),
#                                     albu.OneOf([
#                                         albu.RGBShift(),
#                                         albu.HueSaturationValue(),
#                                     ], p=0.5),
#                                     ]),
#             'weak': albu.Compose([albu.HorizontalFlip(),
#                                   ]),
#             'geometric': albu.OneOf([albu.HorizontalFlip(always_apply=True),
#                                      albu.ShiftScaleRotate(always_apply=True),
#                                      albu.Transpose(always_apply=True),
#                                      albu.OpticalDistortion(always_apply=True),
#                                      albu.ElasticTransform(always_apply=True),
#                                      ])
#             }

#     aug_fn = augs[scope]
#     crop_fn = {'random': albu.RandomCrop(size, size, always_apply=True),
#                'center': albu.CenterCrop(size, size, always_apply=True)}[crop]
#     pad = albu.PadIfNeeded(size, size)

#     pipeline = albu.Compose([aug_fn, crop_fn, pad], additional_targets={'target': 'image'})

#     def process(a, b):
#         r = pipeline(image=a, target=b)
#         return r['image'], r['target']

#     return process


# def get_normalize():
#     normalize = albu.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]) #albu.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])#
#     normalize = albu.Compose([normalize], additional_targets={'target': 'image'})
#     #normalize_target = albu.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
#     #normalize_target= albu.Compose([normalize_target], additional_targets={ 'target':'image'})

#     def process(a, b):
#         r = normalize(image=a, target=b)
#        # r_t= normalize_target(image=a, target=b)
#         return r['image'], r['target']

#     return process


# def _resolve_aug_fn(name):
#     d = {
#         'cutout': albu.Cutout,
#         'rgb_shift': albu.RGBShift,
#         'hsv_shift': albu.HueSaturationValue,
#         'motion_blur': albu.MotionBlur,
#         'median_blur': albu.MedianBlur,
#         'snow': albu.RandomSnow,
#         'shadow': albu.RandomShadow,
#         'fog': albu.RandomFog,
#         'brightness_contrast': albu.RandomBrightnessContrast,
#         'gamma': albu.RandomGamma,
#         'sun_flare': albu.RandomSunFlare,
#         'sharpen': albu.IAASharpen,
#         'jpeg': albu.JpegCompression,
#         'gray': albu.ToGray,
#         # ToDo: pixelize
#         # ToDo: partial gray
#     }
#     return d[name]


# def get_corrupt_function(config: List[dict]):
#     augs = []
#     for aug_params in config:
#         name = aug_params.pop('name')
#         cls = _resolve_aug_fn(name)
#         prob = aug_params.pop('prob') if 'prob' in aug_params else .5
#         augs.append(cls(p=prob, **aug_params))

#     augs = albu.OneOf(augs)

#     def process(x):
#         return augs(image=x)['image']

#     return process


class get_transforms:
    def __init__(self, size: int, scope: str = 'geometric', crop='random') -> None:
        self.augs = {'strong': albu.Compose([albu.HorizontalFlip(),
                                            albu.ShiftScaleRotate(shift_limit=0.0, scale_limit=0.2, rotate_limit=20, p=.4),
                                            albu.ElasticTransform(),
                                            albu.OpticalDistortion(),
                                            albu.OneOf([
                                                albu.CLAHE(clip_limit=2),
                                                albu.IAASharpen(),
                                                albu.IAAEmboss(),
                                                albu.RandomBrightnessContrast(),
                                                albu.RandomGamma()
                                            ], p=0.5),
                                            albu.OneOf([
                                                albu.RGBShift(),
                                                albu.HueSaturationValue(),
                                            ], p=0.5),
                                            ]),
                    'weak': albu.Compose([albu.HorizontalFlip(),
                                        ]),
                    'geometric': albu.OneOf([albu.HorizontalFlip(always_apply=True),
                                            albu.ShiftScaleRotate(always_apply=True),
                                            albu.Transpose(always_apply=True),
                                            albu.OpticalDistortion(always_apply=True),
                                            albu.ElasticTransform(always_apply=True),
                                            ])
                    }

        aug_fn = self.augs[scope]
        crop_fn = {'random': albu.RandomCrop(size, size, always_apply=True),
                   'center': albu.CenterCrop(size, size, always_apply=True)}[crop]
        pad = albu.PadIfNeeded(size, size)

        self.pipeline = albu.Compose([aug_fn, crop_fn, pad], additional_targets={'target': 'image'})


    def __call__(self, a, b):
        return self.process(a, b)
    

    def process(self, a, b):
        r = self.pipeline(image=a, target=b)
        return r['image'], r['target']
    
    

class get_normalize:
    def __init__(self) -> None:        
        self.normalize = albu.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]) #albu.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])#
        self.normalize = albu.Compose([self.normalize], additional_targets={'target': 'image'})
        #normalize_target = albu.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        #normalize_target= albu.Compose([normalize_target], additional_targets={ 'target':'image'})

    def __call__(self, a, b):
        return self.process(a, b)

    def process(self, a, b):
        r = self.normalize(image=a, target=b)
        # r_t= normalize_target(image=a, target=b)
        return r['image'], r['target']



class get_corrupt_function:
    def __init__(self, config: List[dict]):
        self.augs = []
        for aug_params in config:
            name = aug_params.pop('name')
            cls = self._resolve_aug_fn(name)
            prob = aug_params.pop('prob') if 'prob' in aug_params else 0.5
            self.augs.append(cls(p=prob, **aug_params))

        self.augs = albu.OneOf(self.augs)
    
    def __call__(self, x):
        return self.process(x)

    def _resolve_aug_fn(self, name):
        d = {
            'cutout': albu.Cutout,
            'rgb_shift': albu.RGBShift,
            'hsv_shift': albu.HueSaturationValue,
            'motion_blur': albu.MotionBlur,
            'median_blur': albu.MedianBlur,
            'snow': albu.RandomSnow,
            'shadow': albu.RandomShadow,
            'fog': albu.RandomFog,
            'brightness_contrast': albu.RandomBrightnessContrast,
            'gamma': albu.RandomGamma,
            'sun_flare': albu.RandomSunFlare,
            'sharpen': albu.IAASharpen,
            'jpeg': albu.JpegCompression,
            'gray': albu.ToGray,
            # ToDo: pixelize
            # ToDo: partial gray
        }
        return d[name]
    
    def process(self, x):
        return self.augs(image=x)['image']
    
