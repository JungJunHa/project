2022 관광데이터 AI 경진대회
	월/일	주요 내용	모델	모델 정확도	시사점
					
1	09월 26일	Baseline 코드 해석 및 실행	"이미지 : 4 layer(8,16,32,64) / ReLU / MaxPooling
NLP : Linear 2 layer"	0.6172	"Overfitting 발생(epoch 2부터 val loss 증가)
-> dropout이나 model 용량 줄이기 시도 예정"
2	09월 27일	이미지 크기 조정(128 -> 256) / learning rate 조정	"이미지 : 5 layer(8,16,32,64,64) / ReLU / MaxPooling
NLP : Linear 2 layer"	0.60526	Overfitting 발생(epoch 7부터 val loss 증가), 정확도 감소
3	09월 29일	이미지 모델 구조 개선 / learning rate 조정			
4	10월 2일	dropout 추가			
5	10월 3일	다른 모델 고려			
![image](https://user-images.githubusercontent.com/71584305/194863402-68af82e7-e102-4a2d-a777-dc3fc4f628f3.png)
