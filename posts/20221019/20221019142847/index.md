WebUI 사용법 개인 학습 과정 메모

AI/WebAI/StableDiffusion/사용법



목차
- [1. 통합팩 설치와 실행](#1-통합팩-설치와-실행)
- [2. 통합팩 전용 한글패치 설치](#2-통합팩-전용-한글패치-설치)
- [3. (참고) 통합팩 없이 직접 설치](#3-참고-통합팩-없이-직접-설치)
- [4. Web UI 내부 메뉴 별 설명](#4-web-ui-내부-메뉴-별-설명)
  - [4.1. 최상단 공통 UI](#41-최상단-공통-ui)
    - [4.1.1. Stable Diffusion 체크포인트 리스트](#411-stable-diffusion-체크포인트-리스트)
    - [4.1.2. Enable Autocomplete 체크박스](#412-enable-autocomplete-체크박스)
  - [4.2. 텍스트 -> 이미지 메뉴](#42-텍스트---이미지-메뉴)
    - [4.2.1. 프롬프트 입력란](#421-프롬프트-입력란)
    - [프롬프트 입력 관련 편의기능](#프롬프트-입력-관련-편의기능)
    - [4.2.2. 샘플링 스텝 수, 샘플링 방법](#422-샘플링-스텝-수-샘플링-방법)
    - [4.2.3. 이미지 해상도](#423-이미지-해상도)
    - [플러그인](#플러그인)
    - [배치 수(Batch count), 배치 크기(Batch size)](#배치-수batch-count-배치-크기batch-size)
    - [CFC 스케일(CFC Scale)](#cfc-스케일cfc-scale)
    - [시드(Seed)](#시드seed)
    - [생성(Generate)](#생성generate)
    - [결과창](#결과창)
- [5. 각종 에러 상황에 대한 대처](#5-각종-에러-상황에-대한-대처)
  - [5.1. RuntimeError: CUDA out of memory](#51-runtimeerror-cuda-out-of-memory)
    - [5.1.1. 현상](#511-현상)
    - [5.1.2. 원인](#512-원인)
    - [5.1.3. 대처](#513-대처)
- [6. 프롬프트 모음](#6-프롬프트-모음)
  - [6.1. 메인 프롬프트](#61-메인-프롬프트)
    - [6.1.1. 통합팩 기본 메인 프롬프트](#611-통합팩-기본-메인-프롬프트)
  - [6.2. 부정 프롬프트](#62-부정-프롬프트)
    - [6.2.1. 통합팩 기본 부정 프롬프트](#621-통합팩-기본-부정-프롬프트)
    - [6.2.2. 중국발 부정 프롬프트](#622-중국발-부정-프롬프트)
- [프롬프트, 설정 관련 유용한 외부 사이트](#프롬프트-설정-관련-유용한-외부-사이트)
  - [Deep Danbooru (프롬프트)](#deep-danbooru-프롬프트)
- [7. AI 그림 프롬프트 공유 사이트](#7-ai-그림-프롬프트-공유-사이트)
- [8. 기타 각종 설정 관련 짤 모음](#8-기타-각종-설정-관련-짤-모음)
- [9. 참고자료](#9-참고자료)


# 1. 통합팩 설치와 실행
[원본글 링크(아카라이브)](https://arca.live/b/aiart/60216616)

1. "필수 설치파일"의 WEBUI.zip 을 웹 링크를 통해서 다운로드. 설치.ps1 (PowerShell) 실행해서 설치. 

2. 설치가 완료되면 http://0.0.0.0:7860/ 문구가 나오고, http://127.0.0.1:7860/ Running 관련 문구가 나옴.
![](2022-10-19-23-52-10.png)

3. 현재 사용중인 PC의 로컬 호스트의 7860 포트를 통해 Web UI 서버가 동작 중이라는 것이므로 해당 주소로 접속하면 Web UI를 볼 수 있음.

4. 설치 이후에는 .tar 파일은 삭제해도 됨.

5. 향후 Web UI를 실행할 때는 webui가 설치된 폴더의 webui.bat 배치파일을 실행. (웹페이지는 자동으로 오픈됨)



# 2. 통합팩 전용 한글패치 설치
[원본글 링크(아카라이브)](https://arca.live/b/aiart/61057817)

통합팩 설치했으면 필요없지만, 나중에 한글패치 업데이트되면 아래 절차로 적용.


1. 구글 드라이브 링크에서 한글패치 json 파일 다운로드 [한글패치 링크(구글 드라이브)](https://drive.google.com/file/d/1ycx3cy_hLOQt04f5MK13XPJXyqALrcTk/view?usp=sharing)
2. webui 루트 폴더 / localizations 폴더에 해당 파일을 붙여넣기
   ![](2022-10-23-19-35-13.png)
3. Web UI 실행해서 설정 창으로 이동, 스크롤 내려서 Localization 설정을 찾은 후 ko-KR로 반드시 설정창 최상단의 "설정 적용하기" 버튼 클릭.
4. 변경된 설정 적용을 위해 Web UI 재시작. 한글패치 적용 확인.
5. 만약 이미 ko-KR로 적용되어 있어서, 한글패치 복붙해도 적용이 안된다면, Localization 설정을 None 으로 한번 변경 후 재시작, 그후 다시 ko-KR로 변경 후 재시작을 하면 적용됨.
6. 아무래도 설정 쪽은 번역이 안된 모양이다.





# 3. (참고) 통합팩 없이 직접 설치

[AUTOMATIC1111 GitHub 페이지](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

참고로만 알아둘 것. 통합팩이 훨씬 편리함.

페이지의 Installation and Running -> Automatic Installation on Window 항목 참고 (2022.10.23 기준)

1. [Python 3.10.6](https://www.python.org/downloads/windows/) 설치. 설치 시 "Add Python to PATH" 옵션 반드시 선택.
2. [git](https://git-scm.com/download/win) 설치
3. 커맨드라인에서 아래 git 명령어 입력하고 github 링크로 리포지토리 clone 해서 받음
```
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```
4. 모델 체크포인트 파일들(확장자 .ckpt)를 models 폴더에 넣음
  
     [애니메 관련 모델 파일 리포지토리(Hugging Face)](https://huggingface.co/jcink0418/Arca2)
   - [animefull-final-pruned.tar](https://huggingface.co/jcink0418/Arca2/resolve/main/animefull-final-pruned.tar) : 일반적인 상황. 일반짤 ~ R-18까지 광범위 하게 사용가능
   - [animefull-latest.tar](https://huggingface.co/jcink0418/Arca2/resolve/main/animefull-latest.tar) : 일반적인 상황. 일반짤 ~ R-18까지 광범위 하게 사용가능. 중국발 부정 프롬프트 도배시 사용
   
   [runwayml의 stable-diffusion-v1-5 리포지토리](https://huggingface.co/runwayml/stable-diffusion-v1-5)
   - [v1-5-pruned.ckpt](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.ckpt)

5. 실행은 web-user.bat 으로 진행






# 4. Web UI 내부 메뉴 별 설명
## 4.1. 최상단 공통 UI
![](2022-10-23-20-20-28.png)

### 4.1.1. Stable Diffusion 체크포인트 리스트
![](2022-10-23-20-21-02.png)
webui 루트 폴더/models/Stable-diffusion 폴더에 있는 체크포인트 파일(확장자 ckpt)을 참고해서, 이미지 생성에서 사용할 모델을 설정하는 부분. 

### 4.1.2. Enable Autocomplete 체크박스
![](2022-10-23-21-05-38.png)
![](2022-10-23-21-04-28.png)
프롬프트 입력 시 자동완성 기능을 활성화/비활성화 체크박스

## 4.2. 텍스트 -> 이미지 메뉴
![](2022-10-23-21-06-14.png)

### 4.2.1. 프롬프트 입력란
![](2022-10-23-21-13-48.png)
상단이 메인 프롬프트 입력란, 하단이 부정 프롬프트 입력란. 메인 프롬프트에 입력된 텍스트들을 기반으로 이미지를 생성하며, 이 과정에서 부정 프롬프트 입력란을 참고하여 부정적 요소를 제거하는 방향으로 처리가 진행된다.

### 프롬프트 입력 관련 편의기능
![](2022-10-24-07-41-34.png)

프롬프트의 입력과 관련된 몇가지 편의기능이 제공되고 있다. 

**(1) 랜덤 아티스트 추가**

![](2022-10-24-07-43-22.png)

artists.csv 에 나열된 아티스트 이름 중 하나를 무작위로 선택해 프롬프트에 삽입한다.

**(2) 직전 프롬프트 불러오기**

![](2022-10-24-07-46-07.png)

프롬프트 란(메인 및 부정)이 비어있을 경우 바로 직전 세대(last generation)에서 사용되었던 프롬프트를 다시 가져와서 프롬프트 란을 채운다. 실수로 프롬프트 내용들을 삭제했을 경우의 편의기능이다.

프롬프트 란이 메인, 부정 모두 완전히 다 비어 있을때 제대로 동작한다.

**(3) 현재 사용된 프롬프트를 스타일로 저장**

![](2022-10-24-07-53-55.png)

현재 입력된 메인 및 부정 프롬프트 내용을 이름을 지정해서 스타일로서 styles.csv 파일에 저장한다. 저장된 스타일은 "생성(Generate)" 버튼 아래에서 스타일 지정 후 생성 기능 실행하면, 해당 스타일의 프롬프트 내용들과 현재 설정값(시드값 등)을 사용해서 이미지를 생성한다.

저장은 UI에서 가능하지만, 삭제는 styles.csv 파일을 직접 열어서 삭제해야 한다. 아래는 styles.csv 를 엑셀로 열어본 내용이다. 스타일 이름(name)과 메인 프롬프트(prompt), 부정 프롬프트(negative_prompt) 가 column 으로 설정되어 있다.

![](2022-10-24-12-37-47.png)

**(4) 현재 선택된 스타일을 프롬프트 입력란에 적용**

![](2022-10-24-12-27-55.png)

"생성(Generate)" 버튼 아래 있는 UI에서 선택한 스타일의 프롬프트 내용을 프롬프트 입력란에 적용한다.


### 4.2.2. 샘플링 스텝 수, 샘플링 방법
![](2022-10-23-22-06-02.png)

샘플링은 간단히 말해서 이미지를 만드는 과정이라고 생각하면 된다. AI가 이미지를 몇 스텝동안, 무슨 방식으로 만들어낼지 정하는 부분이다.

**(1) 샘플링 스텝 수**

스텝이 높을수록 퀄리티가 좋아지고(디테일, 화질이 좋아짐) 속도가 느려진다. SD 기본모델에서는 80, 90, 120까지도 돌려도 된다. 하지만 유출모델은 2D위주라 그런지 스텝이 너무 높으면 과잉계산?으로 퀄이 떨어지는 경우도 있으니 기본은 28로 놓고 늘리면서 자기 목표에 맞는 값을 찾을 것.


**(2) 샘플링 방법**

어떤 알고리즘을 통해서 이미지를 만들어낼거냐 하는것이다. 해외커뮤니티 많은 유저들은 Euler_a, DDIM을 가장 퀄리티 좋게 뽑힌다고 하니 이걸 쓰도록 하자.


### 4.2.3. 이미지 해상도
![](2022-10-23-22-23-34.png)
보이는 그대로 이미지의 해상도를 정한다(가로 및 세로). 해상도가 클수록 VRAM 점유와 결과 출력 속도가 느려진다. 인물의 경우 크기를 너무 크게 잡으면 인체구조가 박살나는 문제가 있다. 
유출판 기준 512 X 768을 놓고 보통 쓰는데 조금씩 바꿔가면서 써보자.


### 플러그인
![](2022-10-23-22-26-16.png)

**(1) 얼굴 보정(Restore faces)**
얼굴 이상하게 나오는거 교정해주는 플러그인

**(2) 타일링(Tiling)**
닉값대로 뭔 이상한 타일 패턴이 나옴 그냥 없는셈쳐라

**(3) 고해상도 보정(Highres.fix)**
 해상도 커지면 인체 구조 박살나거나 그런 경우에 어느정도 잡아주는 플러그인

플러그인들은 전부 SD 기본모델용으로 만들어졌기 때문에 유출판이나 WD모델에서는 만족스러운 결과가 안나올 수 있으니 되면 좋고 안되면 말고 느낌으로 시도해보자

### 배치 수(Batch count), 배치 크기(Batch size)
![](2022-10-23-23-06-58.png)

batch count는 한번에 뽑아낼 묶음 갯수를 의미함 3이라면 grid에 이미지가 3개씩 묶여서 나오고 6이라면 6개씩 묶여서 나옴

batch size는 batch count를 몇번 돌릴지 결정한다

그러니까 총 결과물 갯수는 batch count X batch size만큼 나옴

![](2022-10-23-23-08-58.png)

이런게 grid임 이건 batch count가 4인경우 더 값을 크게 주면 한번에 grid로 묶이는 그림이 늘어난다


### CFC 스케일(CFC Scale)
![](2022-10-23-23-10-52.png)

AI가 유저가 넣은 프롬프트 입력값을 얼마나 따를지를 결정한다. 높으면 프롬프트에 나온 내용을 대체로 준수하면서 그림을 만들려고 하고, 낮으면 AI가 어느 정도 해석의 자유를 가지고 좀더 다양한 그림을 만들려고 한다.

너무 낮은값을 주면 프롬프트랑 별 상관없는게 나오게 되고 너무 높게 주면 너무 단순한 결과물(프롬프트 내용빼고는 아무것도 없다던가 그림체도 좀 투박한 느낌)을 내놓는다.

### 시드(Seed)

![](2022-10-24-07-57-13.png)


시드(Seed) 값은 AI의 계산에 변수를 줘서 다양한 결과물이 나오게 유도하는 값이다. 다른 세팅값이 다 같아도 시드가 다르면 다른 결과물이 나온다. 이미지 품질에는 기본적으로 영향을 주지 않는 값이지만 운 좋게 퀄리티가 좋게 나오는 시드값을 발견할 수도 있다.

기본으로 -1(랜덤)로 설정되어있다. 여기에 특정 시드 값을 입력할 수 있다.

![](2022-10-24-07-56-48.png)

시드와 관련된 편의기능들이다.

(1) 랜덤값 설정(주사위 아이콘) : 랜덤 시드 설정값 (-1)을 시드 입력란에 넣는다.

(2) 직전 시드 값을 불러오기 (재활용 아이콘) : 직전 세대(last generation)에서 사용된 시드 값을 시드 입력란에 넣는다.

이미지 생성의 결과물 아래의 정보란에서 해당 이미지에 사용된 시드 값을 확인할 수 있다. 해당 시드 값을 직접 복사할수도 있고, 


다른 사람이 공유한 값을 쓰면 그 사람과 같은 결과물을 얻을 수 있는 기본을 갖추는것이다(다른 조건들도 같아야함).



### 생성(Generate)
![](2022-10-24-07-37-19.png)

말 그대로, 프롬프트와 설정들을 가지고 이미지 생성 작업을 진행하는 버튼이다. 

스타일1, 스타일2는 styles.csv 파일에 저장된 스타일 목록을 보여주며, 스타일을 선택 후 생성을 실행하면 스타일에 설정된 프롬프트 내용과 현재 설정(시드 등)에 맞춰서 생성한다.

![](2022-10-24-13-03-42.png)

생성 버튼을 누르면 생성이 시작된다. 생성 작업 진행중에 표시되는 버튼들에 대해 알아보자.
(1) "중단(Interrupt)" : 생성 작업을 도중에 멈추는 기능이다.
(2) "건너뛰기(Skip)" : 설정으로 지정된 샘플링 스탭 수를 모두 진행하지 않고, 건너뛰기를 실행한 시점에서 스탭 진행을 중단하고 그대로 결과물을 출력한다.

샘플링 스텝 수를 28로 하고, 동일한 프롬프트와 시드 값을 설정하고, 도중에 건너뛰기를 실행한 경우와, 끝까지 작업을 실행한 경우의 결과물을 비교해보자. 건너뛰기를 실행한 경우엔 스텝을 끝까지 진행하지 않아 형태가 비교적 무너진 결과물을 보인다.

첫번째 예시이다.

![](2022-10-24-13-12-07.png)
![](2022-10-24-13-12-18.png)


두번째 예시에선 좀더 차이가 분명하다.

![](2022-10-24-13-13-31.png)
![](2022-10-24-13-13-37.png)


### 결과창

![](2022-10-24-13-01-47.png)

(1) 결과물 이미지

프롬프트와 설정대로 AI가 생성한 이미지(혹은 이미지'들')이 표시되는 부분이다.

(2) 



# 5. 각종 에러 상황에 대한 대처
## 5.1. RuntimeError: CUDA out of memory
### 5.1.1. 현상
이미지 생성 실행했는데 런타임 에러 표기됨. 

### 5.1.2. 원인
이미지 생성을 위해 할당할 수 있는 그래픽카드 잔여 메모리(VRAM) 부족으로 인한 에러. 

1. 진짜 그래픽카드 장치의 총 VRAM가 낮은 것이 원인.
2. 혹은 총 VRAM에 비해 용량이 너무 큰 모델을 선택해서 로드 중이라서 그만큼 잔여 VRAM 용량이 부족해진 것일 수 있다.

"작업 관리자" -> "성능" 탭 -> GPU 0 을 선택하고 "전용 GPU 메모리"를 보면 잔여 메모리를 확인할 수 있다. 

예시)

그래픽카드 : RTX 3070 ti (VRAM 8GB)

사용 모델 : animefull-final-prunded.ckpt

Web UI : 일반 모드 (저사양 옵션 X)

아래는 생성을 아직 안했을때의 메모리 상태이다.
![](2022-10-23-23-49-23.png)

아래는 이미지 생성 과정에서 측정된 메모리 상태이다.
![](2022-10-23-23-50-36.png)

1. 생성하려는 이미지의 해상도가 클 경우에도 그만큼 생성 과정에서 VRAM을 차지하기 때문에 


### 5.1.3. 대처
**(1) 그래픽카드 장치의 총 메모리가 낮은 경우의 대처**

실행용 배치파일(webui-user.bat)의 COMMANDLINE_ARGS에 --lowvram 옵션을 추가한다. (통합팩에서는 저사양용 배치파일이 이미 있다.)

일반 배치파일과 저사양용 배치파일의 COMMANDLINE_ARGS 부분을 비교해보자.

```
// 일반 배치파일
set COMMANDLINE_ARGS=--listen --deepdanbooru --autolaunch

// 저사양용 배치파일 
set COMMANDLINE_ARGS=--skip-torch-cuda-test --no-half --precision=full --listen --lowvram --deepdanbooru --autolaunch
```

AUTOMATIC1111의 web ui 공식 설명에서는 아래와 같이 대처방법이 기술되어 있음.
```
VRAM이 낮은 GPU에 대한 최적화. 이렇게 하면 4GB 메모리가 있는 비디오 카드에서 512x512 이미지를 생성할 수 있습니다.

--lowvram는 유저 basujindal 의 최적화 아이디어를 재구현한 것 입니다. 모델은 모듈들로 분리되며, GPU 메모리에는 하나의 모듈만 보관됩니다. 다른 모듈을 실행해야 하는 경우 이전 모듈이 GPU 메모리에서 제거됩니다. 이 최적화의 특성으로 인해 처리가 느리게 실행됩니다. RTX 3090에서 일반 작업에 비해 약 10배 더 느립니다.

--medvram는 동일한 배치(batch)에서 조건부 및 무조건 노이즈 제거 처리를 하지 않음으로써 VRAM 사용량을 크게 줄이는 또 다른 최적화입니다.

이 최적화 구현에서는 원본 Stable Diffusion 코드를 수정할 필요가 없습니다.
```

**(2) 용량이 좀더 적은 모델을 선택한다**

Stable Diffusion 체크포인트 메뉴에서 현재 모델보다 더 용량이 적은 모델을 선택 후 Web UI 재시작한다.


**(3) 생성하려는 이미지 해상도를 줄인다**

512 X 768을 놓고 보통 쓰는데 이보다 크거나 같은데 용량 부족이 발생한다면 해상도를 줄여보자.



# 6. 프롬프트 모음

## 6.1. 메인 프롬프트

### 6.1.1. 통합팩 기본 메인 프롬프트
```
masterpiece, best quality
```


## 6.2. 부정 프롬프트

### 6.2.1. 통합팩 기본 부정 프롬프트
```
lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name
```

### 6.2.2. 중국발 부정 프롬프트
이 때는 모델을 animefull-latest로 사용.
```
multiple breasts, (mutated hands and fingers:1.5), (long body :1.3), (mutation, poorly drawn :1.2), black-white, bad anatomy, liquid body, liquid tongue, disfigured, malformed, mutated, anatomical nonsense, text font ui, error, malformed hands, long neck, blurred, lowers, low res, bad anatomy, bad proportions, bad shadow, uncoordinated body, unnatural body, fused breasts, bad breasts, huge breasts, poorly drawn breasts, extra breasts, liquid breasts, heavy breasts, missing breasts, huge haunch, huge thighs, huge calf, bad hands, fused hand, missing hand, disappearing arms, disappearing thigh, disappearing calf, disappearing legs, fused ears, bad ears, poorly drawn ears, extra ears, liquid ears, heavy ears, missing ears, fused animal ears, bad animal ears, poorly drawn animal ears, extra animal ears, liquid animal ears, heavy animal ears, missing animal ears, text, ui, error, missing fingers, missing limb, fused fingers, one hand with more than 5 fingers, one hand with less than 5 fingers, one hand with more than 5 digit, one hand with less than 5 digit, extra digit, fewer digits, fused digit, missing digit, bad digit, liquid digit, colorful tongue, black tongue, cropped, watermark, username, blurry, JPEG artifacts, signature, 3D, 3D game, 3D game scene, 3D character, malformed feet, extra feet, bad feet, poorly drawn feet, fused feet, missing feet, extra shoes, bad shoes, fused shoes, more than two shoes, poorly drawn shoes, bad gloves, poorly drawn gloves, fused gloves, bad cum, poorly drawn cum, fused cum, bad hairs, poorly drawn hairs, fused hairs, big muscles, ugly, bad face, fused face, poorly drawn face, cloned face, big face, long face, bad eyes, fused eyes poorly drawn eyes, extra eyes, malformed limbs, more than 2 nipples, missing nipples, different nipples, fused nipples, bad nipples, poorly drawn nipples, black nipples, colorful nipples, gross proportions. short arm, (((missing arms))), missing thighs, missing calf, missing legs, mutation, duplicate, morbid, mutilated, poorly drawn hands, more than 1 left hand, more than 1 right hand, deformed, (blurry), disfigured, missing legs, extra arms, extra thighs, more than 2 thighs, extra calf, fused calf, extra legs, bad knee, extra knee, more than 2 legs, bad tails, bad mouth, fused mouth, poorly drawn mouth, bad tongue, tongue within mouth, too long tongue, black tongue, big mouth, cracked mouth, bad mouth, dirty face, dirty teeth, dirty pantie, fused pantie, poorly drawn pantie, fused cloth, poorly drawn cloth, bad pantie, yellow teeth, thick lips, bad camel toe, colorful camel toe, bad asshole, poorly drawn asshole, fused asshole, missing asshole, bad anus, bad pussy, bad crotch, bad crotch seam, fused anus, fused pussy, fused anus, fused crotch, poorly drawn crotch, fused seam, poorly drawn anus, poorly drawn pussy, poorly drawn crotch, poorly drawn crotch seam, bad thigh gap, missing thigh gap, fused thigh gap, liquid thigh gap, poorly drawn thigh gap, poorly drawn anus, bad collarbone, fused collarbone, missing collarbone, liquid collarbone, strong girl, obesity, worst quality, low quality, normal quality, liquid tentacles, bad tentacles, poorly drawn tentacles, split tentacles, fused tentacles, missing clit, bad clit, fused clit, colorful clit, black clit, liquid clit, QR code, bar code, censored, safety panties, safety knickers, beard, furry,pony, pubic hair, mosaic, excrement, faeces, shit, futa, testis
```




# 프롬프트, 설정 관련 유용한 외부 사이트

## Deep Danbooru (프롬프트)
![](2022-10-23-22-29-12.png)
![](2022-10-23-22-29-52.png)
http://dev.kanotype.net:8003/deepdanbooru/
2D 이미지에서 Danbooru 기반 프롬프트 텍스트 추천




# 7. AI 그림 프롬프트 공유 사이트
https://lexica.art/

![](2022-10-23-18-27-16.png)


검색 란에 원하는 바와 비슷한 그림 올리면, 비슷한 AI 그림들과 사용 프롬프트 표시됨
![](2022-10-23-18-26-30.png)


# 8. 기타 각종 설정 관련 짤 모음
![](2022-10-23-18-25-41.png)

![](2022-10-23-18-36-30.png)


# 9. 참고자료

[AUTOMATIC1111의 WEB UI Github 링크](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

[AUTOMATIC1111의 WEB UI Github 위키](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki)

[SD RESOURCE GOLDMINE](https://rentry.org/sdupdates)

[Hugging Fate(SD 모델 파일 배포처)](https://huggingface.co/)

[인공지능 기본 - GAN 과 Diffusion model, Generative Model](https://arca.live/b/aiart/59916341)

[webui 튜토리얼 txt2img 기능설명 기초(아카라이브)](https://arca.live/b/aiart/60273123)