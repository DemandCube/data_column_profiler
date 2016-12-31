class ColumnProfiler(object):
    """
    Abstract base class for all operators. 
    :param task_id: a unique, meaningful id for the task
    :type task_id: string

    """
    
    def __init__(
        self,
        task_id,
        ):
        pass
    
    @classmethod
    def validate(cls):
        """ Not needed but wanted the example
        """
        if not cls.name:
            raise RuntimeError("Your plugin needs a name.")
            
    def add_quality_check(self, check):
        """
        
        """
        if not isinstance(check, QualityCheck):
            raise TypeError(
                        'Expected QualityCheck; received {}'.format(check.__class__.__name__))
        raise NotImplementedError("")
    
    def remove_quality_check(self, check):
        """
        
        """
        raise NotImplementedError("")

    def add_value(self, value):
        """
        
        """
        raise NotImplementedError("")

    def results(self):
        """
        should return and dictionary of dictionaries
        
        {"check_name":{"min_size":"10"}}
        
        """
        raise NotImplementedError("")
    
    def reset(self):
        """
        clears all quality checks states
        """
        raise NotImplementedError("")


# Quality Checks
# - size: min, max avg
# - range: min, max
# - matched
# - mismatched
# - total
# - blanks
# - confidence
# - distribution(histogram)
# - missing
# - outliers
# - uniques
# - frequency
# - valid
# - size: min, lower quartile, median, upper quartile, max, avg, stdeviation


class QualityCheck(object):
    """
    Abstract base class for all operators. 
    :param task_id: a unique, meaningful id for the task
    :type task_id: string

    """
    
    def __init__(
        self,
        task_id,
        ):
        pass

    def add_value(self, value):
        """
        
        """
        raise NotImplementedError("")

    def results(self):
        """
        should return and dictionary of dictionaries
        
        {"check_name":{"min_size":"10"}}
        
        """
        raise NotImplementedError("")
    
    def reset(self):
        """
        clears all quality checks states
        """
        raise NotImplementedError("")
        
    def get_max_size(self, value):
        """
        
        """
        raise NotImplementedError("")