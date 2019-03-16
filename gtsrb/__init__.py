from gtsrb.trainer import Trainer
from gtsrb.model import Gtsrb

if __name__ == '__main__':
    model = Gtsrb()          # Gtrsb 클래스를 가져옴
    dataset = model.read_dataset('images/', model.N_CLASSES, model.RESIZE_IMAGE) # images 폴더 안에 있는 모든 데이터를 가져옴
    trainer = Trainer(model) # trainer에 model을 줌
    trainer.execute()        # trainer를 실행함




