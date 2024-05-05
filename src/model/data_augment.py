class DataAugment:
    def __init__(self, input_frames: str, output_frames: str):
        """
        Initialize the DataAugment class with the input and output frames
        Args:
            input_frames (str): The input frames folder
            output_frames (str): The output frames folder
        """
        self.input_frames = input_frames
        self.output_frames = output_frames
    
    def resize(self):
        """
        Resize the input frames to a smaller size (640x640)
        """
        pass
