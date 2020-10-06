{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "# loading Python Imaging Library \n",
    "from PIL import ImageTk, Image\n",
    "# To get the dialog box to open when required  \n",
    "from tkinter import filedialog "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def openfilename():\n",
    "    # open file dialog box to select image\n",
    "    # The dialogue box has a title \"Open\"\n",
    "    filename = filedialog.askopenfilename(title ='Select the image for classification')\n",
    "    return filename"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "class frame_set(Frame):\n",
    "    \n",
    "    def __init__(self, master, *pargs):\n",
    "        Frame.__init__(self, master, *pargs)\n",
    "        x = openfilename() \n",
    "        self.image = Image.open(x)\n",
    "        self.img_copy= self.image.copy()\n",
    "        self.background_image = ImageTk.PhotoImage(self.image)\n",
    "        self.background = Label(self, image=self.background_image)\n",
    "        self.background.pack(fill=BOTH, expand=NO)\n",
    "        self.background.bind('<Configure>', self._resize_image)\n",
    "\n",
    "    def _resize_image(self,event):\n",
    "        new_width = event.width\n",
    "        new_height = event.height\n",
    "        self.image = self.img_copy.resize((new_width, new_height))\n",
    "        self.background_image = ImageTk.PhotoImage(self.image)\n",
    "        self.background.configure(image =  self.background_image)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "root = Tk()\n",
    "root.title(\"Image Classification\")\n",
    "root.geometry(\"600x600\")\n",
    "root.configure(background=\"gray\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "e = frame_set(root)\n",
    "e.pack(fill=BOTH, expand=YES)\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
