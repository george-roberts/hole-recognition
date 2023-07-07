#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        holes = adsk.cam.RecognizedHole
        ent = ui.selectEntity('Select body', 'Bodies')
        recognized = holes.recognizeHoles([ent.entity])
        ui.activeSelections.clear()
        hole = recognized.item(0)
        for hole in recognized:
            info = ""
            info += "Top diameter = " + str(hole.topDiameter) + "\n"
            info += "Bottom diameter = " + str(hole.bottomDiameter) + "\n"
            info += "Through hole = " + str(hole.isThrough) + "\n"
            info += "Threaded hole = " + str(hole.isThreaded) + "\n"
            info += "Number of segments = " + str(hole.segmentCount) + "\n"
            info += "Errors = " + str(hole.hasErrors) + "\n"
            info += "Warnings = " + str(hole.hasWarnings) + "\n"
            for segment in range(hole.segmentCount):
                holeSegment = hole.segment(segment)
                for face in holeSegment.faces:
                    ui.activeSelections.add(face)

            ui.messageBox(info)
            ui.activeSelections.clear()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
