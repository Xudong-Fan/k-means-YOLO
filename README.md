# convert_2_YOLO

Convert Pascal VOC annotation to [Yolo Darknet](https://pjreddie.com/darknet/yolo/) format.
​    

## Required Parameters

Each dataset requries some parameters

1. --datasets

   - like COCO / VOC

     ```bash
     --datasets VOC
     ```

2. --img_path

   - the directory holding all the images

     ```bash
     --img_path ./VOC/JPEGImages/
     ```

3. --label

   - the directory holding all the annotation files

     ```bash
     --label ./VOC/Annotations/
     ```

4. --convert_output_path

   - it directory path. not file path

     ```bash
     --convert_output_path ./
     ```

5. --img_type

   - like `.png`, `.jpg`

     ```bash
     --img_type ".jpg"
     ```

6. --records_path

   - paths of treated images

     ```bash
     --records_path ./
     ```

7. --cla_list_file(`*.names`)

   - it is `*.names` file contain class names. refer [darknet `*.name` file](https://github.com/pjreddie/darknet/blob/master/data/voc.names)

     ```bash
     --cls_list_file voc.names
     ```

​    

## Example of usage​    

### 1. Description of dataset directory

Suppose that VOC dataset location is `./VOC`,

here is the structure for `VOC`
​    
**`VOC`**

```bash
└── VOC
    ├── Annotations
    └── JPEGImages
```

- Annotations : Object Detection label folder
- JPEGImages : Image data
​    
**Annotations**

```bash
├── 000001.xml
├── 000002.xml
├── 000003.xml
...
└── 001000.xml
```

**JPEGImages**

```bash
├── 000001.jpg
├── 000002.jpg
├── 000003.jpg
...
└── 001000.jpg
```

​
### 2. Create file or folder

**Make `*.names` file in `./VOC/`**，refer [darknet `voc.names` file](https://github.com/pjreddie/darknet/blob/master/data/voc.names)

```bash
aeroplane
bicycle
bird
boat
bottle
bus
car
cat
chair
cow
diningtable
dog
horse
motorbike
person
pottedplant
sheep
sofa
train
tvmonitor
```
​    
**Make `./YOLO` folder**
    

### 3. Command

```bash
python convert-2-yolo.py --datasets VOC --img_path ./VOC/JPEGImages/ --label ./VOC/Annotations/ --convert_output_path ./YOLO/ --img_type ".jpg" --records_path ./ --cls_list_file ./VOC/voc.names

VOC Parsing:   |████████████████████████████████████████| 100.0% (1000/1000) Complete
YOLO Generating:|████████████████████████████████████████| 100.0% (1000/1000)Complete
YOLO Saving:   |████████████████████████████████████████| 100.0% (1000/1000) Complete
```

​    
### 4. Result

Check result files (`./YOLO/` and `./records.txt`)

**`./YOLO/`**

```bash
├── 000001.txt
├── 000002.txt
├── 000003.txt
...
└── 001000.txt
```
​    
**`./records.txt`**

```bash
F:\Master_Beihang\xml_2_yolo\VOC\JPEGImages\000001.jpg
F:\Master_Beihang\xml_2_yolo\VOC\JPEGImages\000002.jpg
F:\Master_Beihang\xml_2_yolo\VOC\JPEGImages\000003.jpg
...
F:\Master_Beihang\xml_2_yolo\VOC\JPEGImages\001000.jpg
```


### TODO

**Refactoring (Release v2.0.0)**
- [ ] Rewrite README.md for more helpful use
- [ ] Support more dataset types
- [ ] Skip object class that don't want

