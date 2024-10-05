from django import forms
from .models import ImageUploadModel


class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    # ImageField는 FileFiled로부터 모든 속성과 함수를 상속받지만,업로드된 이미지가 유효한 이미지인지 증명한다.
    # file = forms.FileField()
    image = forms.ImageField()


class ImageUploadForm(forms.ModelForm):
    # Form을 통해 받아들여야 할 데이터가 명시되어 있는 메타 데이터(DB table을 연결)
    class Meta:
        model = ImageUploadModel
        # Form을 통해 사용자로부터 입력 받으려는 Model Class의 field 리스트
        fields = ('description', 'document',)  # uploaded_at